# Chain of Responsibility design pattern

## Description

The Chain of Responsibility pattern is a behavioral design pattern that allows a request to be passed along a chain of handlers until one of the handlers processes it. Each handler has a chance to handle the request or forward it to the next handler, decoupling the sender of the request from its receivers.

## What specific problems do I solve using this pattern?

The Chain of Responsibility pattern addresses scenarios where multiple objects may handle a request and the specific handler isn't known a priori. It allows for dynamic arrangement of handlers, promotes loose coupling between sender and receiver, and enables flexible handling policies that can be changed without modifying the sender.

## Can I combine this design pattern with others? Which ones?

The Chain of Responsibility pattern can be combined with other patterns:

- Composite: Chain of Responsibility can be used within composite structures where parent components forward requests to children or vice versa
- Decorator: Handlers can be wrapped to add responsibilities while maintaining the chain
- Observer: Handlers can publish events when they process requests
- Strategy: Different chain configurations can be swapped using Strategy
- Factory Method: Chains can be created by factories to initialize handler sequences

## Contents of this section

The implementation in `main.py` demonstrates the Chain of Responsibility pattern through a UI help system example with the following components:

`ComponentWithContextualHelp`: Abstract interface for components that can provide contextual help via `show_help()`.

`Component`: Base component that stores optional `tooltip_text` and a reference to a parent container. Its `show_help()` method either prints its tooltip, delegates to its container, or indicates no tips are available.

`Container`: Extends `Component` to hold child components. It provides an `add()` method to attach children and set their container reference.

`Button`: Simple UI component extending `Component`.

`Panel`: A container that may provide modal help text; its `show_help()` overrides behavior to prefer modal help.

`Dialog`: A top-level container that can provide a wiki URL for help; its `show_help()` overrides behavior to prefer the wiki URL.

`Application`: Constructs a sample UI composed of `Dialog`, `Panel`, and `Button` instances, and demonstrates how pressing F1 on different components triggers help resolution through the chain.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.