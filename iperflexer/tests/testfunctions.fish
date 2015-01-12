function transferfeature
    cd ../
    tangleweave iperfparser.pnw
    tangleweave sumparser.pnw
    cd tests/steps
    tangleweave transferfeature.pnw
    cd ../
    behave features/transfer.feature
end
