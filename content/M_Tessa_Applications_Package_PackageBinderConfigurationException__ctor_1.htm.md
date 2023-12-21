# PackageBinderConfigurationException(SerializationInfo, StreamingContext) -
конструктор
Initializes a new instance of the
[PackageBinderConfigurationException](T_Tessa_Applications_Package_PackageBinderConfigurationException.htm)
class. Инициализирует новый экземпляр класса
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) с
сериализованными данными.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected PackageBinderConfigurationException(
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
    PackageBinderConfigurationException(
    	[NotNullAttribute] SerializationInfo^ info, 
    	StreamingContext context
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] info : SerializationInfo * 
            context : StreamingContext -> PackageBinderConfigurationException
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
[PackageBinderConfigurationException -
](T_Tessa_Applications_Package_PackageBinderConfigurationException.htm)
[PackageBinderConfigurationException -
перегрузка](Overload_Tessa_Applications_Package_PackageBinderConfigurationException__ctor.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
