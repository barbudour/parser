# CommandArgumentException.GetObjectData - метод
When overridden in a derived class, sets the
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
with information about the exception.
##  __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override void GetObjectData(
    	SerializationInfo info,
    	StreamingContext context
    )
VB __Копировать
     Public Overrides Sub GetObjectData ( 
    	info As SerializationInfo,
    	context As StreamingContext
    )
C++ __Копировать
     public:
    virtual void GetObjectData(
    	SerializationInfo^ info, 
    	StreamingContext context
    ) override
F# __Копировать
     abstract GetObjectData : 
            info : SerializationInfo * 
            context : StreamingContext -> unit 
    override GetObjectData : 
            info : SerializationInfo * 
            context : StreamingContext -> unit 
#### Параметры
info
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
    The [SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo) that holds the serialized object data about the exception being thrown.
context
[StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)
    The [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext) that contains contextual information about the source or destination.
#### Реализации
[ISerializable.GetObjectData(SerializationInfo,
StreamingContext)](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable.getobjectdata#system-
runtime-serialization-iserializable-getobjectdata\(system-runtime-
serialization-serializationinfo-system-runtime-serialization-
streamingcontext\))  
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
The info parameter is a null reference (null in Visual Basic).  
---|---  
[SecurityException](https://learn.microsoft.com/dotnet/api/system.security.securityexception)|
The caller does not have the required permission.  
##  __См. также
#### Ссылки
[CommandArgumentException -
](T_Tessa_Platform_CommandLine_CommandArgumentException.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
