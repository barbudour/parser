# PipeXmlMessage - класс
Базовый класс для сообщения, передаваемого по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class PipeXmlMessage : IPipeXmlMessage, 
    	IPipeMessage, ISealable
VB __Копировать
     Public MustInherit Class PipeXmlMessage
    	Implements IPipeXmlMessage, IPipeMessage, ISealable
C++ __Копировать
     public ref class PipeXmlMessage abstract : IPipeXmlMessage, 
    	IPipeMessage, ISealable
F# __Копировать
     [<AbstractClassAttribute>]
    type PipeXmlMessage = 
        class
            interface IPipeXmlMessage
            interface IPipeMessage
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeXmlMessage
Derived
[Tessa.Platform.Pipes.PipeXmlRequest](T_Tessa_Platform_Pipes_PipeXmlRequest.htm)
[Tessa.Platform.Pipes.PipeXmlResponse](T_Tessa_Platform_Pipes_PipeXmlResponse.htm)
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm), [IPipeXmlMessage](T_Tessa_Platform_Pipes_IPipeXmlMessage.htm)
##  __Конструкторы
[PipeXmlMessage](M_Tessa_Platform_Pipes_PipeXmlMessage__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[IsSealed](P_Tessa_Platform_Pipes_PipeXmlMessage_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
---|---  
[Item](P_Tessa_Platform_Pipes_PipeXmlMessage_Item.htm)|  Возвращает или
устанавливает параметр сообщения по заданному ключу. Если параметр
отсутствует, то возвращает null.  
[RootElementName](P_Tessa_Platform_Pipes_PipeXmlMessage_RootElementName.htm)|
Имя корневого xml-элемента для сообщения.  
[Values](P_Tessa_Platform_Pipes_PipeXmlMessage_Values.htm)|  Список параметров
сообщения.  
[XmlSerializer](P_Tessa_Platform_Pipes_PipeXmlMessage_XmlSerializer.htm)|
Объект, используемый для сериализации и десериализации текущего объекта в
форме XML.  
## __Методы
[CheckSealed](M_Tessa_Platform_Pipes_PipeXmlMessage_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
---|---  
[ClearValues](M_Tessa_Platform_Pipes_PipeXmlMessage_ClearValues.htm)|  Удаляет
все параметры сообщения, установленные ранее.  
[ContainsValue](M_Tessa_Platform_Pipes_PipeXmlMessage_ContainsValue.htm)|
Возвращает признак того, что заданный параметр присутствует в сообщении.  
[Deserialize](M_Tessa_Platform_Pipes_PipeXmlMessage_Deserialize.htm)|
Десериализует сообщение из строковой формы.  
[DeserializeFromXml](M_Tessa_Platform_Pipes_PipeXmlMessage_DeserializeFromXml.htm)|
Десериализует сообщение из формы XML.  
[DeserializeXmlCore](M_Tessa_Platform_Pipes_PipeXmlMessage_DeserializeXmlCore.htm)|
Выполняет десериализацию объекта из XML.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValues](M_Tessa_Platform_Pipes_PipeXmlMessage_GetValues.htm)|  Возвращает
список параметров в сообщении с указанием имени параметра и его значения.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveValue](M_Tessa_Platform_Pipes_PipeXmlMessage_RemoveValue.htm)|  Удаляет
параметр из сообщения. Возвращает признак того, что он присутствовал и был
удалён.  
[Seal](M_Tessa_Platform_Pipes_PipeXmlMessage_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Platform_Pipes_PipeXmlMessage_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[Serialize](M_Tessa_Platform_Pipes_PipeXmlMessage_Serialize.htm)|  Сериализует
сообщение в строковой форме.  
[SerializeToXml](M_Tessa_Platform_Pipes_PipeXmlMessage_SerializeToXml.htm)|
Сериализует сообщение в форме XML.  
[SerializeXmlCore](M_Tessa_Platform_Pipes_PipeXmlMessage_SerializeXmlCore.htm)|
Выполняет сериализацию объекта в XML.  
[ToString](M_Tessa_Platform_Pipes_PipeXmlMessage_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
