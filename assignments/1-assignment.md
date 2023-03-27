### 1.1 Introduction
The goals of this homework are to develop an understanding a communications model, data communications, networks, protocol architecture as well as the basic concepts of data transmissions, data rate, bandwidth and channel capacity.

### 1.2 Briefly explain the advantages and disadvantages of using layered architecture in computer networks.
Computer networking is a complex architecture, it composes of software, firmware, hardware, and electric signals. To manage this complexity computer networks are organized in multiple layers. These multiple layers are build in such way so that these feels like one upon another layer.

#### Advantages of layered architecture in computer networks
A few of easily noticeable features of the layered architecture are modularity and easily distinguishable interfaces. Each layer is responsible for performing a single individual task, for example, the session layer is designed to maintain the session between hosts placed at remote locations.

```
| Layered Architecture

[Layer C] <--Peer Layer--> [Layer C]
    ^                        ^
    |                        |
   Inter  layer  communication
    |                        |
    v                        v
[Layer B] <--Peer Layer--> [Layer B]
    ^                        ^
    |                        |
   Inter  layer  communication
    |                        |
    v                        v
[Layer A] <--Peer Layer--> [Layer A]
```

It become very easy for testing and troubleshooting as well since if task is initiated by top layer, it processes the task and sends to lower layer or other way around. Layered architecture offers independence for each layer involved, which means in case of maintenance, upgrade, replacement of an existing layer can be done without affecting all other layers.

The layers are made of basic components such as interfaces, protocols, and services. Services provides a set of features offered to its higher layer. Protocols are a set of rules for transferring or exchanging of data with a peer entity. Each layer has a defined service interface to send data from one layer to another layer. The benefit of sub-components architecture in a layer is to further upgrade of each layer without replacing entire layer.

A protocol data unit (PDU) is required to establish communication between two adjacent layers. A PDU can be attached at the head or tail of a message or data. This process of adding or removing PDU is known as encapsulation or decapsulation. The advantage of defining a PDU for each layer helps the host systems to process the information in a well defined environment. For example, if the data moves downwards in source system and other way around in destination system.

Layered architecture of computer networks makes it easy to develop independently since different teams can work in parallel.

Network security becomes easy to implement since all layered behave independently. Different layers can be deployed on different machines to enhance security posture and improve performance. Network scaling also becomes cakewalk because of layered architecture.

In Open System Interconnect (OSI) is an open standard for all computer networks and it was introduced by International Standard Organization (ISO). It has seven layers, application (top), presentation, session, transport, network, data-link, physical (bottom) layers. OSI model benefits us in implementing layered computer networks or it is baseline of all newer layered computer networks.

Disadvantages of layered architecture in computer networks
It becomes difficult to process large amount of data because of heavy resource consumption. Or in other words the main disadvantage is processing data in different layers and data overhead. It would require to invoke all seven layers involved in OSI model. Data overhead is another disadvantage because of protocol headers or trails.

Each layer requires minimum one protocol, which causes delay in development of layer features.

Even after the layers are independent still tasks can not be performed in parallel. Each layer has to wait to process data one after another layer.

Duplication of services and layer features such as transport layer and data link layer both the layers have error control processes. Another example is presentation and session layers, both layers deals with session and user management. Both layers can be fused together because layering is not as useful as other layers in OSI model.

Poor inter layer communication could be one reason for imposing additional data overhead, for example VPNs poor performance.

Introduction of newer protocol has become very difficult in OSI model. For example WebSocket protocol specification IETF 6455 defines that it operates over HTTP. It creates a dependency on HTTP. SMTP is another example which enforces requirements from RFC 5321.

### 1.3 What tasks are performed by the data link layer and the transport layer? 
Open Systems Interconnection (OSI) reference model was introduced by International Standard Organization (ISO) as an international standard for computer network communication architecture.

The OSI reference model has seven layers

* Application
* Presentation
* Session
* Transport
* Network
* Data link
* Physical

#### Tasks performed by Data Link Layer
- The data link layer takes responsibility for organizing bits into frames to transmit from one to the next node.
- This layer rectifies the physical layer to appear fault free to the network layer.

```
| From network layer to physical layer


        Network layer
             |
             v
[Header | Data | Trail ] <-- Frame (Data link layer)
             |
             v
        Physical layer
```

```
| From physical layer to network layer


        Network layer
             ^
             |
[Header | Data | Trail ] <-- Frame (Data link layer)
             ^
             |
        Physical layer
```

- The data link layer packages data from physical layer into blocks, frames or packets. If the data is transmits to another system on the network then this layer adds up necessary information to the header such as physical address of the source or destination system.
- This layer makes it possible to route data by attaching information headers between remotely placed devices in a network environment while utilizing networks, and/or subnetworks. Added header information helps systems/networks to transmit data to the correct source/destination systems.
- This layer provides different types of controls such as flow, access, and error control. For example, IEEE 802 LAN (Local Area Network) has well-explained MAC (Media Access Control) and LLC (Logical Link Control) sublayers. Because of this IEEE 802 layers (such as Ethernet) fits well with IEEE 802.2 LLC protocol.

##### Data Link Layer's Sublayers
- Media Access Control Sublayer
- Logical Link Layer Sublayer

###### Media Access Control Sublayer
MAC (Media Access Control) is responsible for controlling media access at any one time. MAC can be subdivided into distributed and centralized. MAC takes care of frame synchronization, which means while bit-streaming MAC determines the start and end of data frames (It utilizes timing-based detection or character counting, or byte stuffing, or bit stuffing).

###### Logical Link Control Sublayer
LLC (Logical Link Control) sublayer specifies processes to be used in addressing stations over the transmission medium. It optionally controls flow, acknowledgment, error messages. This sublayer comes at the top of Data Link Layer.

##### Error Detection and Correction
If provided, Data Link Layer may perform error detection as well. To avail of error detection sender must add an error detection code. Once the data frame is received, the receiver verifies the error detection code to detect the error.

#### Tasks performed by Transport Layer
- The transport layer provides a system's process to process communication and error recovery.
- The transport layer takes care of end-to-end data message delivery between two devices on a network. As well this layer ensures transparent data transfer from one endpoint to another.

```
| From application layer to network layer

                Application layer
        ---------------------------------
        |               |               |
        v               v               v
[ [Data | Header] [Data | Header] [Data | Header] ] <-- Segments (Transport layer)
        |               |               |
        v               v               v
        ---------------------------------
                    Physical layer
```

```
| From network layer to application layer

                Application layer
        ---------------------------------
        ^               ^               ^
        |               |               |
[ [Data | Header] [Data | Header] [Data | Header] ] <-- Segments (Transport layer)
        ^               ^               ^
        |               |               |
        ---------------------------------
                    Physical layer
```

- Transport layer's responsibilities
	- Message routing
	- Data segmenting
	- Error recovery
	- Basic services for Application layer protocol
		- Connection oriented
		- Connectionless
	- May provide
		- Data tracking
		- Connection flow control
		- Sequencing of data
		- Error checking
		- Application addressing and identification
- The highly famous transport layer protocol TCP (Transport Control Protocol) comes from Internet Protocol suites and is used for connection-oriented data transmissions, whereas connectionless UDP (User Datagram Protocol) is used for simple message transfers. TCP is complex and known for reliable data transfers.
- Transport layer provide services such as
	- Connection oriented communication,
	- Same order delivery,
	- Congestion avoidance,
	- Reliability,
	- Multiplexing,
	- Flow control.

1.4 Draw (by hand) the spectrum of the signal s(t) = 4sin(2πt) + 2sin(6πt) + 8/π sin(7πt). Also identify the absolute and effective bandwidths.
The spectrum of the signal describes changes in signal's magnitude and phase as a function of frequency.

Spectrum of the signal
s(t)    = 4sin(2πt) + 2sin(6πt) + 8/π sin(7πt)

Absolute bandwidth is not always the appropriate measure of bandwidth because it is the width of the spectrum.
Effective bandwidth is either the actual bandwidth or speed at which data can be transmitted over a connection.
In the above because of finite numbers of frequency Absolute bandwidth is same as effective bandwidth.

High frequency - Low frequency = Absolute bandwidth = Effective bandwidth
							 = fhigh - flow
							 = 3.5 - 1
							 =  2.5 Hz

### 1.5 What is the channel capacity for a teleprinter channel with a 300Hz bandwidth and a signal-to-noise ratio of 3 dB, where the noise is a white thermal noise?
Channel capacity can be calculated using Shannon-Hartley theorem. Shannon-Hartley is credited as a father of modern information age. Channel capacity is maximum rate of data transmitted over a communication channel of a defined bandwidth. Channel capacity considers presence of thermal noise. Channel capacity is measured in bits per second.

```
| Shannon's Equation

Channel Capacity = B * log(1 + SNR)
```

Solution
- Bandwidth (B) = 300Hz
- Signal to noise ratio (SNR) = 3dB

Channel Capacity = 300 * log(1 + 3)
                 = 300 * log(4)
                 = 300 * 2
                 = 600 bits per second

The channel capacity for a teleprinter channel with a 300Hz bandwidth and a signal-to-noise ratio of 3 dB, where the noise is a white thermal noise, is 600 bits per second.

### 1.6 A digital signaling system is required to operate at 9600 bps. If the signal encodes a 4-bit word, what is the minimum required bandwidth of that channel?
Bandwidth (in a digital signaling system) is the difference between higher and lower frequencies in a continuous range and is measured in Hertz unit.

Formula to calculate minimum required bandwidth:
	
Ba    = fs/2

Solution
- The sampling rate (fs) = R/n
- Operation rate of digital signaling system (R) = 9600 bits per second
- The Number of bits (n) = 4

fs     = 9600/4
	= 2400Hz
	
Ba    = 2400/2
	= 1200Hz

A digital signaling system is required to operate at 9600 bps. If the signal encodes a 4-bit word, the minimum required bandwidth of the channel is 1200Hz.
