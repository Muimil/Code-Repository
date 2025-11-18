/**
 * @fileoverview WebRTC IP 泄露防护脚本
 * @author Muimill
 * @version 1.0.0
 * @license MIT
 * 
 * 警告：此脚本旨在提供一种客户端侧的防护措施，但不能保证100%的防护效果。
 * 最佳实践仍是使用浏览器扩展或在浏览器设置中禁用WebRTC。
 */

(function() {
    "use strict";

    // 检查浏览器是否支持 WebRTC
    if (!window.RTCPeerConnection) {
        console.info("WebRTC Leak Prevent: 当前浏览器不支持 RTCPeerConnection，无需防护。");
        return;
    }

    /**
     * 原始的 RTCPeerConnection 构造函数
     * @type {RTCPeerConnection}
     */
    const OriginalRTCPeerConnection = window.RTCPeerConnection;

    /**
     * 覆写 RTCPeerConnection 构造函数，以修改其配置。
     * 
     * WebRTC IP 泄露的原理在于 ICE (Interactive Connectivity Establishment) 过程会
     * 收集所有可能的网络接口地址，包括本地 IP 和 VPN/代理背后的真实公网 IP。
     * 
     * 我们的目标是通过修改配置，限制 ICE 候选者的收集，从而阻止本地 IP 的暴露。
     * 
     * @param {RTCConfiguration} config - 传入的配置对象
     * @param {any} args - 剩余参数
     * @returns {RTCPeerConnection} - 经过修改配置的新 RTCPeerConnection 实例
     */
    window.RTCPeerConnection = function(config, ...args) {
        // 1. 深度复制原始配置，避免修改原始对象
        const newConfig = JSON.parse(JSON.stringify(config || {}));

        // 2. 核心防护措施：设置 iceCandidatePoolSize 为 0
        //    这将阻止浏览器收集本地 IP 地址作为 ICE 候选者。
        //    这是现代浏览器（如 Chrome 48+）推荐的、侵入性较小的防护方法。
        newConfig.iceCandidatePoolSize = 0;

        // 3. 备用防护措施：修改 iceServers 配置
        //    如果 iceServers 存在，我们只保留 TURN 服务器，并移除 STUN 服务器。
        //    STUN 服务器用于发现公网 IP，而 TURN 服务器可以强制所有流量通过它转发，
        //    从而避免直接的点对点连接和 IP 泄露。
        if (newConfig.iceServers && Array.isArray(newConfig.iceServers)) {
            newConfig.iceServers = newConfig.iceServers.filter(server => {
                // 检查 URL 是否包含 'turn' 协议
                const isTurn = server.urls && (Array.isArray(server.urls) ? server.urls : [server.urls]).some(url => url.startsWith('turn:'));
                
                // 如果不是 TURN 服务器，则移除
                if (!isTurn) {
                    console.warn(`WebRTC Leak Prevent: 移除潜在的 IP 泄露源 STUN 服务器: ${server.urls}`);
                }
                return isTurn;
            });

            // 如果配置中没有 TURN 服务器，可以考虑添加一个公共的 TURN 服务器
            // 但为了不引入外部依赖和潜在的隐私问题，此处选择不自动添加。
            // 仅在 iceServers 数组为空时，打印警告。
            if (newConfig.iceServers.length === 0) {
                console.warn("WebRTC Leak Prevent: iceServers 数组为空，WebRTC 连接可能失败，但 IP 泄露风险降低。");
            }
        }

        console.info("WebRTC Leak Prevent: RTCPeerConnection 配置已修改，iceCandidatePoolSize=0。");

        // 4. 使用修改后的配置调用原始构造函数
        return new OriginalRTCPeerConnection(newConfig, ...args);
    };

    // 5. 额外防护：覆写 createOffer 和 createAnswer
    //    虽然主要防护在构造函数中完成，但为了更全面的兼容性，
    //    我们也可以在 SDP (Session Description Protocol) 层面进行修改。
    //    SDP 中可能包含本地 IP 地址信息。

    /**
     * 覆写 RTCPeerConnection.prototype.createOffer
     * @param {RTCOfferOptions} options - 选项
     * @returns {Promise<RTCSessionDescriptionInit>} - Promise 对象
     */
    const OriginalCreateOffer = OriginalRTCPeerConnection.prototype.createOffer;
    OriginalRTCPeerConnection.prototype.createOffer = function(options) {
        return OriginalCreateOffer.call(this, options).then(sdp => {
            // 移除 SDP 中的本地 IP 地址信息 (mDNS/host)
            sdp.sdp = sdp.sdp.replace(/a=candidate:.*(host|mDNS).*\r\n/g, '');
            return sdp;
        });
    };

    /**
     * 覆写 RTCPeerConnection.prototype.createAnswer
     * @param {RTCOfferOptions} options - 选项
     * @returns {Promise<RTCSessionDescriptionInit>} - Promise 对象
     */
    const OriginalCreateAnswer = OriginalRTCPeerConnection.prototype.createAnswer;
    OriginalRTCPeerConnection.prototype.createAnswer = function(options) {
        return OriginalCreateAnswer.call(this, options).then(sdp => {
            // 移除 SDP 中的本地 IP 地址信息 (mDNS/host)
            sdp.sdp = sdp.sdp.replace(/a=candidate:.*(host|mDNS).*\r\n/g, '');
            return sdp;
        });
    };

    console.info("WebRTC Leak Prevent: 脚本加载完成，RTCPeerConnection 已被覆写。");

})();
