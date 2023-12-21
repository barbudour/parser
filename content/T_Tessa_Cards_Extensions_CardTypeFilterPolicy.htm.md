# CardTypeFilterPolicy - класс
Политика фильтрации расширений, использующая политику
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm) для того,
чтобы не выполнять методы расширений, для которых в контексте
[ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm)
использовано имя типа карточки, запрещённое указанной политикой, или тип
карточки неизвестен. Если политика
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm) не
зарегистрирована, то метод расширения выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardTypeFilterPolicy : IFilterPolicy, 
    	IExtensionPolicy
VB __Копировать
     Public NotInheritable Class CardTypeFilterPolicy
    	Implements IFilterPolicy, IExtensionPolicy
C++ __Копировать
     public ref class CardTypeFilterPolicy sealed : IFilterPolicy, 
    	IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type CardTypeFilterPolicy = 
        class
            interface IFilterPolicy
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardTypeFilterPolicy
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm), [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm)
##  __Конструкторы
[CardTypeFilterPolicy](M_Tessa_Cards_Extensions_CardTypeFilterPolicy__ctor.htm)|
Инициализирует новый экземпляр класса CardTypeFilterPolicy  
---|---  
##  __Свойства
[Instance](P_Tessa_Cards_Extensions_CardTypeFilterPolicy_Instance.htm)|
Экземпляр класса.  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[FilterAsync](M_Tessa_Cards_Extensions_CardTypeFilterPolicy_FilterAsync.htm)|
Возвращает признак того, что выполнение метода с заданным параметром разрешено
для экземпляра расширения.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetFilterContextAsync](M_Tessa_Cards_Extensions_CardTypeFilterPolicy_GetFilterContextAsync.htm)|
Возвращает контекст фильтрации, используемый для определение разрешений на
выполнение метода для экземпляров расширений.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
