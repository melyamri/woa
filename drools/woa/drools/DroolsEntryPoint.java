package woa.drools;

import py4j.GatewayServer;

import org.drools.KnowledgeBase;
import org.drools.KnowledgeBaseFactory;
import org.drools.builder.KnowledgeBuilder;
import org.drools.builder.KnowledgeBuilderError;
import org.drools.builder.KnowledgeBuilderErrors;
import org.drools.builder.KnowledgeBuilderFactory;
import org.drools.builder.ResourceType;
import org.drools.io.ResourceFactory;
import org.drools.runtime.StatefulKnowledgeSession;


public class DroolsEntryPoint {

    public DroolsEntryPoint() {
    }

    private KnowledgeBase getKnowledgeBase(String file)  throws Exception {
        return readKnowledgeBase(file);
    }

    public StatefulKnowledgeSession getKnowledgeSession(String file)  throws Exception {
        return getKnowledgeBase(file).newStatefulKnowledgeSession();
    }

    private KnowledgeBase readKnowledgeBase(String file) throws Exception {

        KnowledgeBuilder kbuilder = KnowledgeBuilderFactory.newKnowledgeBuilder();

        kbuilder.add(ResourceFactory.newClassPathResource(file), ResourceType.DRL);

        KnowledgeBuilderErrors errors = kbuilder.getErrors();

        if (errors.size() > 0) {
           for (KnowledgeBuilderError error: errors) {
              System.err.println(error);
           }
           throw new IllegalArgumentException("Could not parse knowledge.");
        }

        KnowledgeBase kbase = KnowledgeBaseFactory.newKnowledgeBase();
        kbase.addKnowledgePackages(kbuilder.getKnowledgePackages());

        return kbase;
     }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new DroolsEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}
