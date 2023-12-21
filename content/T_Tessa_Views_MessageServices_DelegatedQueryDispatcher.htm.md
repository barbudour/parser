# DelegatedQueryDispatcher - класс
Диспетчер запросов с возможностью перенаправления запросов
##  __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DelegatedQueryDispatcher : IQueryDispatcher
VB __Копировать
     Public NotInheritable Class DelegatedQueryDispatcher
    	Implements IQueryDispatcher
C++ __Копировать
     public ref class DelegatedQueryDispatcher sealed : IQueryDispatcher
F# __Копировать
     [<SealedAttribute>]
    type DelegatedQueryDispatcher = 
        class
            interface IQueryDispatcher
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DelegatedQueryDispatcher
Implements
    [IQueryDispatcher](T_Tessa_Views_MessageServices_IQueryDispatcher.htm)
##  __Конструкторы
[DelegatedQueryDispatcher](M_Tessa_Views_MessageServices_DelegatedQueryDispatcher__ctor.htm)|
Инициализирует новый экземпляр класса DelegatedQueryDispatcher  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Execute<TResult>](M_Tessa_Views_MessageServices_DelegatedQueryDispatcher_Execute__1.htm)|
Осуществляет попытку выполнения запроса  
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
[IsRegistered<TQuery>](M_Tessa_Views_MessageServices_DelegatedQueryDispatcher_IsRegistered__1.htm)|
Осуществляет проверку наличия обработчика для запросаа  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Register](M_Tessa_Views_MessageServices_DelegatedQueryDispatcher_Register.htm)|
Осуществляет регистрацию обработчика запроса  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetHandler<TQuery,
TResult>](M_Tessa_Views_MessageServices_DelegatedQueryDispatcher_TryGetHandler__2.htm)|
Осуществляет попытку получения обработчика для запроса TQuery с результатом
выполнения TResult  
[UnRegister<TQuery>](M_Tessa_Views_MessageServices_DelegatedQueryDispatcher_UnRegister__1.htm)|
Осуществляет удаление регистрации обработчика запроса  
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
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
