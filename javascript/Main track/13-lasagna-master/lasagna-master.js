/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(timer) {
    switch (timer) {
        case undefined:
            return "You forgot to set the timer.";
        case 0:
            return "Lasagna is done.";
        default:
            return "Not done, please wait.";
    }
}

export function preparationTime(layers, avgTime = 2) {
    return layers.length * avgTime;
}

export function quantities(layers) {
    let noodles = 0, sauce = 0;
    for (let layer of layers) {
        switch (layer) {
            case "noodles":
                noodles += 50;
                break;
            case "sauce":
                sauce += 0.2;
                break;
        }
    }
    return {"noodles": noodles, "sauce": sauce};
}

export function addSecretIngredient(friendsList, myList) {
    myList.push(friendsList[friendsList.length - 1]);
}

export function scaleRecipe(recipe, nPortions) {
    let scaledRecipe = {};
    let factor = nPortions / 2;
    for (const key in recipe) {
        scaledRecipe[key] = factor  * recipe[key];
    }
    return scaledRecipe;
}