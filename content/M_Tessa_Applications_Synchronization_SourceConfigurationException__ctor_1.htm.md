# SourceConfigurationException(SerializationInfo, StreamingContext) -
конструктор
Initializes a new instance of the
[SourceConfigurationException](T_Tessa_Applications_Synchronization_SourceConfigurationException.htm)
class. Инициализирует новый экземпляр класса
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) с
сериализованными данными.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected SourceConfigurationException(
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
    SourceConfigurationException(
    	[NotNullAttribute] SerializationInfo^ info, 
    	StreamingContext context
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] info : SerializationInfo * 
            context : StreamingContext -> SourceConfigurationException
#### Параметры
info
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo)
     Объект [SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo), содержащий сериализованные данные объекта о создаваемом исключении. 
context
[StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext)
     Объект [StreamingContext](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext), содержащий контекстные сведения об источнике или назначении. 
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Значение параметра info — null.  
---|---  
[SerializationException](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationexception)|
Имя класса — null или
[HResult](https://learn.microsoft.com/dotnet/api/system.exception.hresult#system-
exception-hresult) равно нулю (0).  
## __См. также
#### Ссылки
[SourceConfigurationException -
](T_Tessa_Applications_Synchronization_SourceConfigurationException.htm)
[SourceConfigurationException -
перегрузка](Overload_Tessa_Applications_Synchronization_SourceConfigurationException__ctor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
