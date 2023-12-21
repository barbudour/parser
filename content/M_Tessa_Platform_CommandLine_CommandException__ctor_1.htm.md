# CommandException(SerializationInfo, StreamingContext) - конструктор
Initializes a new instance of the CommandException class with serialized data.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CommandException(
    	SerializationInfo info,
    	StreamingContext context
    )
VB __Копировать
     Protected Sub New ( 
    	info As SerializationInfo,
    	context As StreamingContext
    )
C++ __Копировать
     protected:
    CommandException(
    	SerializationInfo^ info, 
    	StreamingContext context
    )
F# __Копировать
     new : 
            info : SerializationInfo * 
            context : StreamingContext -> CommandException
#### Параметры
info
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
    The object that holds the serialized object data.
context
[StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)
    The contextual information about the source or destination.
##  __См. также
#### Ссылки
[CommandException - ](T_Tessa_Platform_CommandLine_CommandException.htm)
[CommandException -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandException__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
