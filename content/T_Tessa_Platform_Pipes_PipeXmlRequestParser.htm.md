# PipeXmlRequestParser - класс
Объект, выполняющий десериализацию объекта запроса из текста.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeXmlRequestParser : IPipeRequestParser
VB __Копировать
     Public Class PipeXmlRequestParser
    	Implements IPipeRequestParser
C++ __Копировать
     public ref class PipeXmlRequestParser : IPipeRequestParser
F# __Копировать
     type PipeXmlRequestParser = 
        class
            interface IPipeRequestParser
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeXmlRequestParser
Implements
    [IPipeRequestParser](T_Tessa_Platform_Pipes_IPipeRequestParser.htm)
##  __Заметки
Наследники класса могут переопределить методы объекта.
## __Конструкторы
[PipeXmlRequestParser](M_Tessa_Platform_Pipes_PipeXmlRequestParser__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[MessageFactory](P_Tessa_Platform_Pipes_PipeXmlRequestParser_MessageFactory.htm)|
Фабрика объектов, используемых для создания сообщений, передаваемых по каналу.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryParse](M_Tessa_Platform_Pipes_PipeXmlRequestParser_TryParse.htm)|
Десериализует из заданного текста объект запроса. Возвращает null, если текст
не содержит подходящего объекта. Тип объекта может отличаться в зависимости от
того, какие данные были сериализованы.  
[TryParseCore](M_Tessa_Platform_Pipes_PipeXmlRequestParser_TryParseCore.htm)|
Десериализует из заданного XML-элемента объект ответа на запрос. Возвращает
null, если XML-элемент не содержит подходящего объекта. Тип объекта может
отличаться в зависимости от того, какие данные были сериализованы.  
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
