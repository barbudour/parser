# PipeHelper - класс
Вспомогательные методы для использования совместно с каналами API Pipes.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PipeHelper
VB __Копировать
     Public NotInheritable Class PipeHelper
C++ __Копировать
     public ref class PipeHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type PipeHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeHelper
##  __Методы
[DeserializeDataContractFromPipeMessage(Type,
XElement)](M_Tessa_Platform_Pipes_PipeHelper_DeserializeDataContractFromPipeMessage.htm)|
Десериализует значение типа type, отмеченного атрибутом
[DataContractAttribute](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.datacontractattribute),
из XML-элемента serializedValue, который использовался в сообщениях для
передачи по каналу в качестве параметра или возвращаемого значения.  
---|---  
[DeserializeDataContractFromPipeMessage<T>(XElement)](M_Tessa_Platform_Pipes_PipeHelper_DeserializeDataContractFromPipeMessage__1.htm)|
Десериализует значение типа T, отмеченного атрибутом
[DataContractAttribute](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.datacontractattribute),
из XML-элемента serializedValue, который использовался в сообщениях для
передачи по каналу в качестве параметра или возвращаемого значения.  
[SerializeDataContractToPipeMessage(Type,
Object)](M_Tessa_Platform_Pipes_PipeHelper_SerializeDataContractToPipeMessage.htm)|
Сериализует объект, отмеченный атрибутом
[DataContractAttribute](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.datacontractattribute),
в виде XML-элемента
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement),
который может использоваться в сообщениях для передачи по каналу в качестве
параметра или возвращаемого значения.  
[SerializeDataContractToPipeMessage<T>(T)](M_Tessa_Platform_Pipes_PipeHelper_SerializeDataContractToPipeMessage__1.htm)|
Сериализует объект, отмеченный атрибутом
[DataContractAttribute](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.datacontractattribute),
в виде XML-элемента
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement),
который может использоваться в сообщениях для передачи по каналу в качестве
параметра или возвращаемого значения.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
