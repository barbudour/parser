# ViewAccessPolicy<TContext> \- класс
Политика доступности представлений. Поддерживает следующие виды правил.
Открытие обобщенные классы реализующие интерфейс правил вида
[IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm). Закрытые
класс реализующие интерфейс правил вида [IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm) с
подходящими типами. Открытие обобщенные класс реализующие интерфейса правил
[IViewAccessRule<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessRule_1.htm)
Закрытые классы реализующие интерфейса правил
[IViewAccessRule<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessRule_1.htm)
с подходящим контекстом
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ViewAccessPolicy<TContext> : AccessPolicy<ITessaView, TContext>, 
    	IViewAccessPolicy<TContext>, IAccessPolicy<ITessaView, TContext>
VB __Копировать
     Public Class ViewAccessPolicy(Of TContext)
    	Inherits AccessPolicy(Of ITessaView, TContext)
    	Implements IViewAccessPolicy(Of TContext), IAccessPolicy(Of ITessaView, TContext)
C++ __Копировать
    generic<typename TContext>
    public ref class ViewAccessPolicy : public AccessPolicy<ITessaView^, TContext>, 
    	IViewAccessPolicy<TContext>, IAccessPolicy<ITessaView^, TContext>
F# __Копировать
     type ViewAccessPolicy<'TContext> = 
        class
            inherit AccessPolicy<ITessaView, 'TContext>
            interface IViewAccessPolicy<'TContext>
            interface IAccessPolicy<ITessaView, 'TContext>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[AccessPolicy](T_Tessa_Views_AccessPolicy_AccessPolicy_2.htm)<[ITessaView](T_Tessa_Views_ITessaView.htm), TContext> __ ViewAccessPolicy<TContext>
Implements
    [IAccessPolicy](T_Tessa_Views_AccessPolicy_IAccessPolicy_2.htm)<[ITessaView](T_Tessa_Views_ITessaView.htm), TContext>, [IViewAccessPolicy](T_Tessa_Views_AccessPolicy_IViewAccessPolicy_1.htm)<TContext>
#### Параметры типа
TContext
     Тип контекста 
## __Конструкторы
[ViewAccessPolicy<TContext>](M_Tessa_Views_AccessPolicy_ViewAccessPolicy_1__ctor.htm)|
Инициализирует новый экземпляр класса ViewAccessPolicy<TContext>  
---|---  
##  __Методы
[AddRules](M_Tessa_Views_AccessPolicy_AccessPolicy_2_AddRules.htm)|  Добавляет
правила в политику безопасности  
(Унаследован от [AccessPolicy<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_AccessPolicy_2.htm))  
---|---  
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
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_AccessPolicy_2_IsSatisfiedByAsync.htm)|
Осуществляет проверку доступности элемента subject в соответствии с правилами
политик доступа.  
(Унаследован от [AccessPolicy<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_AccessPolicy_2.htm))  
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
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
