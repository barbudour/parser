# PipeXmlResponse - класс
Сообщение-ответ, полученное по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeXmlResponse : PipeXmlMessage, 
    	IPipeResponse, IPipeMessage, ISealable
VB __Копировать
     Public Class PipeXmlResponse
    	Inherits PipeXmlMessage
    	Implements IPipeResponse, IPipeMessage, ISealable
C++ __Копировать
     public ref class PipeXmlResponse : public PipeXmlMessage, 
    	IPipeResponse, IPipeMessage, ISealable
F# __Копировать
     type PipeXmlResponse = 
        class
            inherit PipeXmlMessage
            interface IPipeResponse
            interface IPipeMessage
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm) __ PipeXmlResponse
Derived
[Tessa.Platform.Pipes.PipeBinaryXmlResponse](T_Tessa_Platform_Pipes_PipeBinaryXmlResponse.htm)
[Tessa.Platform.Pipes.PipeXmlExceptionResponse](T_Tessa_Platform_Pipes_PipeXmlExceptionResponse.htm)
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm), [IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm)
##  __Заметки
Наследники класса могут переопределить методы и свойства, а также добавить
дополнительные методы и свойства.
## __Конструкторы
[PipeXmlResponse](M_Tessa_Platform_Pipes_PipeXmlResponse__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[IsSealed](P_Tessa_Platform_Pipes_PipeXmlMessage_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
---|---  
[Item](P_Tessa_Platform_Pipes_PipeXmlMessage_Item.htm)|  Возвращает или
устанавливает параметр сообщения по заданному ключу. Если параметр
отсутствует, то возвращает null.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[RootElementName](P_Tessa_Platform_Pipes_PipeXmlResponse_RootElementName.htm)|
Имя корневого xml-элемента для сообщения.  
(Переопределяет
[PipeXmlMessage.RootElementName](P_Tessa_Platform_Pipes_PipeXmlMessage_RootElementName.htm))  
[Value](P_Tessa_Platform_Pipes_PipeXmlResponse_Value.htm)|  Основное значение,
полученное в ответе на запрос. Это аналог значения, возвращаемого методом в
выражении return.  
[Values](P_Tessa_Platform_Pipes_PipeXmlMessage_Values.htm)|  Список параметров
сообщения.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[XmlSerializer](P_Tessa_Platform_Pipes_PipeXmlMessage_XmlSerializer.htm)|
Объект, используемый для сериализации и десериализации текущего объекта в
форме XML.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
##  __Методы
[CheckSealed](M_Tessa_Platform_Pipes_PipeXmlMessage_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
---|---  
[ClearValues](M_Tessa_Platform_Pipes_PipeXmlMessage_ClearValues.htm)|  Удаляет
все параметры сообщения, установленные ранее.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[ContainsValue](M_Tessa_Platform_Pipes_PipeXmlMessage_ContainsValue.htm)|
Возвращает признак того, что заданный параметр присутствует в сообщении.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[Deserialize](M_Tessa_Platform_Pipes_PipeXmlMessage_Deserialize.htm)|
Десериализует сообщение из строковой формы.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[DeserializeFromXml](M_Tessa_Platform_Pipes_PipeXmlMessage_DeserializeFromXml.htm)|
Десериализует сообщение из формы XML.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[DeserializeXmlCore](M_Tessa_Platform_Pipes_PipeXmlMessage_DeserializeXmlCore.htm)|
Выполняет десериализацию объекта из XML.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
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
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveValue](M_Tessa_Platform_Pipes_PipeXmlMessage_RemoveValue.htm)|  Удаляет
параметр из сообщения. Возвращает признак того, что он присутствовал и был
удалён.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[Seal](M_Tessa_Platform_Pipes_PipeXmlMessage_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[SealInternal](M_Tessa_Platform_Pipes_PipeXmlMessage_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[Serialize](M_Tessa_Platform_Pipes_PipeXmlMessage_Serialize.htm)|  Сериализует
сообщение в строковой форме.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[SerializeToXml](M_Tessa_Platform_Pipes_PipeXmlMessage_SerializeToXml.htm)|
Сериализует сообщение в форме XML.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[SerializeXmlCore](M_Tessa_Platform_Pipes_PipeXmlMessage_SerializeXmlCore.htm)|
Выполняет сериализацию объекта в XML.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
[ToString](M_Tessa_Platform_Pipes_PipeXmlMessage_ToString.htm)| Возвращает
строковое представление объекта.  
(Унаследован от [PipeXmlMessage](T_Tessa_Platform_Pipes_PipeXmlMessage.htm))  
##  __Поля
[ValueKey](F_Tessa_Platform_Pipes_PipeXmlResponse_ValueKey.htm)|  Имя ключа,
по которому записывается значение
[Value](P_Tessa_Platform_Pipes_PipeXmlResponse_Value.htm).  
---|---  
[XmlRootElementName](F_Tessa_Platform_Pipes_PipeXmlResponse_XmlRootElementName.htm)|
Имя корневого элемента в форме XML.  
## __Методы расширения
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
