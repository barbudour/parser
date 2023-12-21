# UnityExtraViewListProvider - класс
Имплементация [провайдера](T_Tessa_Views_IExtraViewListProvider.htm)
представлений задаваемых программным путем. Используется для регистрации в
контейнере для проброса в классы зависящие от
[IExtraViewListProvider](T_Tessa_Views_IExtraViewListProvider.htm) в случае
отсутствия пользовательской регистрации
[провайдера](T_Tessa_Views_IExtraViewListProvider.htm). Всегда возвращает
пустой список [представлений](T_Tessa_Views_ITessaView.htm)
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UnityExtraViewListProvider : IExtraViewListProvider
VB __Копировать
     Public NotInheritable Class UnityExtraViewListProvider
    	Implements IExtraViewListProvider
C++ __Копировать
     public ref class UnityExtraViewListProvider sealed : IExtraViewListProvider
F# __Копировать
     [<SealedAttribute>]
    type UnityExtraViewListProvider = 
        class
            interface IExtraViewListProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UnityExtraViewListProvider
Implements
    [IExtraViewListProvider](T_Tessa_Views_IExtraViewListProvider.htm)
##  __Конструкторы
[UnityExtraViewListProvider](M_Tessa_Views_UnityExtraViewListProvider__ctor.htm)|
Инициализирует новый экземпляр класса UnityExtraViewListProvider  
---|---  
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
[GetExtraViews](M_Tessa_Views_UnityExtraViewListProvider_GetExtraViews.htm)|
Возвращает список программных представлений  
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
