# TextPartReader - класс
Обеспечивает чтение [JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm) из
потока и добавление их в контекст
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm)
##  __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class TextPartReader
VB __Копировать
     Public Class TextPartReader
C++ __Копировать
     public ref class TextPartReader
F# __Копировать
     type TextPartReader = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TextPartReader
##  __Конструкторы
[TextPartReader(Stream)](M_Tessa_Platform_IO_TextPartReader__ctor.htm)|
Инициализирует новый экземпляр класса TextPartReader  
---|---  
[TextPartReader(TextReader)](M_Tessa_Platform_IO_TextPartReader__ctor_1.htm)|
Инициализирует новый экземпляр класса TextPartReader  
##  __Методы
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
[ReadAsync](M_Tessa_Platform_IO_TextPartReader_ReadAsync.htm)|  Осуществляет
чтение JSON-строки из потока и добавление блоков
[Content](P_Tessa_Platform_Json_JsonTextPart_Content.htm) в контекст
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm).
JSON-строкой считается содержимое потока до первого блока [TEXTPART], если он
есть, либо до конца потока. Корректность не проверяется.  
[RevertCharacterReplacement](M_Tessa_Platform_IO_TextPartReader_RevertCharacterReplacement.htm)|
Возвращает содержимое блока TEXTPART в исходный вид до эскейпинга символов.
Строки вида \n\\\\[\\\\[TEXTPART будут превращены в строки \n[TEXTPART.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
