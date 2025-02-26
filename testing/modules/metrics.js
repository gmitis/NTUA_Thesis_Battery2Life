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

// helper function
export const updateMetrics = (isValid, inputValidity) => {
    if (isValid && inputValidity) {
        TP.add(1);
    } else if (!isValid &&  inputValidity) {
        TN.add(1);
    } else if ( isValid && !inputValidity) {
        FP.add(1);
    } else if (!isValid && !inputValidity) {
        FN.add(1);
    }

    const TPV = TP._value;
    const TNV = TN._value;
    const FPV = FP._value;
    const FNV = FN._value;
    const total = TPV + TNV + FPV + FNV;

    if (total > 0) {
        accuracy.add((TPV + TNV) / total);
        misclassification.add((FPV + FNV) / total);
    }
    if (TPV + FPV > 0) precision.add(TPV / (TPV + FPV));
    if (TPV + FNV > 0) sensitivity.add(TPV / (TPV + FNV));
    if (TNV + FPV > 0) specificity.add(TNV / (TNV + FPV));
};
