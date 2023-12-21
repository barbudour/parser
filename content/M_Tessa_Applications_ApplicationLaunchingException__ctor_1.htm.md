# ApplicationLaunchingException(SerializationInfo, StreamingContext) -
конструктор
Initializes a new instance of the
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) class
with serialized data.
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected ApplicationLaunchingException(
    	[NotNullAttribute] SerializationInfo info,
    	StreamingContext context
    )
VB __Копировать
     Protected Sub New ( 
    	<NotNullAttribute> info As SerializationInfo,
    	context As StreamingContext
    )
C++ __Копировать
     protected:
    ApplicationLaunchingException(
    	[NotNullAttribute] SerializationInfo^ info, 
    	StreamingContext context
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] info : SerializationInfo * 
            context : StreamingContext -> ApplicationLaunchingException
#### Параметры
info
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
    The [SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) that holds the serialized object data about the exception being thrown.
context
[StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)
    The [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) that contains contextual information about the source or destination.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
info is null.  
---|---  
[SerializationException](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationexception)|
The class name is null or
[HResult](https://learn.microsoft.com/dotnet/api/system.exception.hresult#system-
exception-hresult) is zero (0).  
##  __См. также
#### Ссылки
[ApplicationLaunchingException -
](T_Tessa_Applications_ApplicationLaunchingException.htm)
[ApplicationLaunchingException -
перегрузка](Overload_Tessa_Applications_ApplicationLaunchingException__ctor.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
