# CardAnyMethodPolicy<TMethod> \- класс
Политика, определяющая для расширений допустимость любого метода выполнения
запроса к API карточек по его вхождению в список допустимых методов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardAnyMethodPolicy<TMethod> : ICardMethodPolicy<TMethod>, 
    	IExtensionPolicy
    where TMethod : struct, new()
VB __Копировать
     Public NotInheritable Class CardAnyMethodPolicy(Of TMethod As {Structure, New})
    	Implements ICardMethodPolicy(Of TMethod), IExtensionPolicy
C++ __Копировать
    generic<typename TMethod>
    where TMethod : value class, gcnew()
    public ref class CardAnyMethodPolicy sealed : ICardMethodPolicy<TMethod>, 
    	IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type CardAnyMethodPolicy<'TMethod when 'TMethod : struct, new()> = 
        class
            interface ICardMethodPolicy<'TMethod>
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardAnyMethodPolicy<TMethod>
Implements
    [ICardMethodPolicy](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)<TMethod>, [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
#### Параметры типа
TMethod
    Тип метода выполнения запроса к API карточек.
##  __Конструкторы
[CardAnyMethodPolicy<TMethod>](M_Tessa_Cards_Extensions_CardAnyMethodPolicy_1__ctor.htm)|
Инициализирует новый экземпляр класса CardAnyMethodPolicy<TMethod>  
---|---  
##  __Свойства
[Instance](P_Tessa_Cards_Extensions_CardAnyMethodPolicy_1_Instance.htm)|
Экземпляр класса.  
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
[IsAllowed](M_Tessa_Cards_Extensions_CardAnyMethodPolicy_1_IsAllowed.htm)|
Проверяет, что заданный метод является допустимым для выполнения расширения.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
