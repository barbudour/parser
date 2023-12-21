# StoreTessaViewRequest - класс
Запрос к сервису [ITessaViewService](T_Tessa_Views_ITessaViewService.htm)
предназначенный для изменения списка представлений
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class StoreTessaViewRequest : IStoreTessaViewRequest, 
    	IStoreModelRequest<TessaViewModel>
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class StoreTessaViewRequest
    	Implements IStoreTessaViewRequest, IStoreModelRequest(Of TessaViewModel)
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class StoreTessaViewRequest : IStoreTessaViewRequest, 
    	IStoreModelRequest<TessaViewModel^>
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type StoreTessaViewRequest = 
        class
            interface IStoreTessaViewRequest
            interface IStoreModelRequest<TessaViewModel>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StoreTessaViewRequest
Derived
[Tessa.Views.ImportTessaViewRequest](T_Tessa_Views_ImportTessaViewRequest.htm)
Implements
    [IStoreModelRequest](T_Tessa_Views_IStoreModelRequest_1.htm)<[TessaViewModel](T_Tessa_Views_TessaViewModel.htm)>, [IStoreTessaViewRequest](T_Tessa_Views_IStoreTessaViewRequest.htm)
##  __Конструкторы
[StoreTessaViewRequest](M_Tessa_Views_StoreTessaViewRequest__ctor.htm)|
Initializes a new instance of the StoreTessaViewRequest class. Инициализирует
новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Свойства
[Models](P_Tessa_Views_StoreTessaViewRequest_Models.htm)|  Gets or sets Список
моделей  
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
