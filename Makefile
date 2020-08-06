RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	cp dome dome.bak
	${RPMBUILD} -ba onemetre-dome-server.spec
	${RPMBUILD} -ba rasa-dome-server.spec
	awk '{sub("DOME = .*$$","DOME = \"onemetre\""); print $0}' dome.bak > dome
	${RPMBUILD} -ba onemetre-dome-client.spec
	awk '{sub("DOME = .*$$","DOME = \"rasa\""); print $0}' dome.bak > dome
	${RPMBUILD} -ba rasa-dome-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-dome.spec
	mv build/noarch/*.rpm .
	mv dome.bak dome
	rm -rf build
