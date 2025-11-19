/**
 * @fileoverview 深度合并（Deep Merge）多个对象的工具函数
 * @author Muimill
 * @version 1.0.0
 * @license MIT
 * 
 * 深度合并是一种递归地将源对象的属性合并到目标对象中的操作。
 * 它不同于浅合并（如 Object.assign() 或展开运算符），后者只会复制顶层属性。
 * 
 * 场景：常用于合并配置对象、更新复杂的应用状态等。
 */

/**
 * 检查一个值是否是纯粹的对象（Plain Object）。
 * @param {*} item - 待检查的值
 * @returns {boolean} - 如果是纯粹的对象则返回 true
 */
function isPlainObject(item) {
    return (item && typeof item === 'object' && !Array.isArray(item) && item.constructor === Object);
}

/**
 * 深度合并两个或多个对象。
 * 
 * 注意：此函数会修改第一个参数（目标对象）。
 * 
 * @param {Object} target - 合并的目标对象，将被修改
 * @param {...Object} sources - 一个或多个源对象
 * @returns {Object} - 合并后的目标对象
 */
function deepMerge(target, ...sources) {
    // 确保目标对象是纯粹的对象，否则返回目标对象本身
    if (!isPlainObject(target)) {
        return target;
    }

    // 遍历所有源对象
    for (const source of sources) {
        // 确保源对象存在且是纯粹的对象
        if (isPlainObject(source)) {
            // 遍历源对象的每一个键值对
            for (const key in source) {
                // 确保属性是源对象自身的属性，而不是继承的
                if (Object.prototype.hasOwnProperty.call(source, key)) {
                    const sourceValue = source[key];
                    const targetValue = target[key];

                    // 1. 如果源属性值和目标属性值都是纯粹的对象，则进行递归合并
                    if (isPlainObject(sourceValue) && isPlainObject(targetValue)) {
                        // 递归调用 deepMerge
                        target[key] = deepMerge(targetValue, sourceValue);
                    } 
                    // 2. 如果源属性值是数组，则直接替换目标属性值（不进行数组内元素的深度合并）
                    else if (Array.isArray(sourceValue)) {
                        // 考虑到数组深度合并的复杂性和不确定性，此处选择直接替换
                        target[key] = sourceValue.slice(); // 使用 slice() 进行浅拷贝，避免引用问题
                    }
                    // 3. 否则，直接用源属性值覆盖目标属性值
                    else {
                        target[key] = sourceValue;
                    }
                }
            }
        }
    }

    return target;
}

// 导出函数，使其可以在 Node.js 或其他模块系统中使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = deepMerge;
} else if (typeof window !== 'undefined') {
    window.deepMerge = deepMerge;
}

// 示例用法（仅作演示，实际使用时可删除）
/*
const defaultSettings = {
    host: 'localhost',
    port: 8080,
    auth: {
        enabled: true,
        secret: 'default-secret'
    },
    plugins: ['log', 'cache']
};

const userSettings = {
    port: 3000,
    auth: {
        secret: 'my-new-secret'
    },
    plugins: ['log', 'db', 'metrics'],
    timeout: 5000
};

const finalSettings = deepMerge(defaultSettings, userSettings);

console.log(finalSettings);
// 预期输出:
// {
//   host: 'localhost',
//   port: 3000,
//   auth: {
//     enabled: true,
//     secret: 'my-new-secret'
//   },
//   plugins: [ 'log', 'db', 'metrics' ], // 数组被替换
//   timeout: 5000
// }
*/
