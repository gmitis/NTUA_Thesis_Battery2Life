import { Counter, Rate } from "k6/metrics";

// T: true, F: false, P: positive, N: negative
export const TP = new Counter("TP");
export const TN = new Counter("TN");
export const FP = new Counter("FP");
export const FN = new Counter("FN");

export const accuracy = new Rate("accuracy");
export const misclassification = new Rate("misclassification");
export const precision = new Rate("precision");
export const sensitivity = new Rate("sensitivity");
export const specificity = new Rate("specificity");

let tpValue = 0;
let tnValue = 0;
let fpValue = 0;
let fnValue = 0;

// helper function
export const updateMetrics = (isValid, inputValidity) => {
    if (isValid && inputValidity) {
        TP.add(1);
        tpValue++;
    } else if (!isValid &&  inputValidity) {
        FN.add(1);
        fnValue++;
    } else if ( isValid && !inputValidity) {
        FP.add(1);
        fpValue++;
    } else if (!isValid && !inputValidity) {
        TN.add(1);
        tnValue++;
    }

    const total = tpValue + tnValue + fpValue + fnValue;

    if (total > 0) {
        accuracy.add((tpValue + tnValue) / total);
        misclassification.add((fpValue + fnValue) / total);
    }
    if (tpValue + fpValue > 0) precision.add(tpValue / (tpValue + fpValue));
    if (tpValue + fnValue > 0) sensitivity.add(tpValue / (tpValue + fnValue));
    if (tnValue + fpValue > 0) specificity.add(tnValue / (tnValue + fpValue));
};
