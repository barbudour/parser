# ImportTessaViewRequest - класс
Реализация запроса к сервису
[ITessaViewService](T_Tessa_Views_ITessaViewService.htm) предназначенного для
импорта представлений
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ImportTessaViewRequest : StoreTessaViewRequest
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ImportTessaViewRequest
    	Inherits StoreTessaViewRequest
C++ __Копировать
    [SerializableAttribute]
    public ref class ImportTessaViewRequest sealed : public StoreTessaViewRequest
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ImportTessaViewRequest = 
        class
            inherit StoreTessaViewRequest
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StoreTessaViewRequest](T_Tessa_Views_StoreTessaViewRequest.htm) __ ImportTessaViewRequest
##  __Конструкторы
[ImportTessaViewRequest](M_Tessa_Views_ImportTessaViewRequest__ctor.htm)|
Инициализирует новый экземпляр класса ImportTessaViewRequest  
---|---  
##  __Свойства
[ImportRoles](P_Tessa_Views_ImportTessaViewRequest_ImportRoles.htm)|  Признак
необходимости импорта списка доступов.  
---|---  
[Models](P_Tessa_Views_StoreTessaViewRequest_Models.htm)|  Gets or sets Список
моделей  
(Унаследован от
[StoreTessaViewRequest](T_Tessa_Views_StoreTessaViewRequest.htm))  
[NeedClear](P_Tessa_Views_ImportTessaViewRequest_NeedClear.htm)|  Признак
необходимости очистки справочника представлений.  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
