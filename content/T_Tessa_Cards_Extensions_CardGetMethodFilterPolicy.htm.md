# CardGetMethodFilterPolicy - класс
Политика фильтрации расширений, использующая политику
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
с типом [CardGetMethod](T_Tessa_Cards_CardGetMethod.htm) для того, чтобы не
выполнять методы расширений, для которых в контексте
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
указан неподходящий метод
[Method](P_Tessa_Cards_Extensions_ICardGetExtensionContext_Method.htm). Если
требуемая политика не зарегистрирована, то метод в контексте проверяется на
равенство значению по умолчанию [Default](T_Tessa_Cards_CardGetMethod.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardGetMethodFilterPolicy : IFilterPolicy, 
    	IExtensionPolicy
VB __Копировать
     Public NotInheritable Class CardGetMethodFilterPolicy
    	Implements IFilterPolicy, IExtensionPolicy
C++ __Копировать
     public ref class CardGetMethodFilterPolicy sealed : IFilterPolicy, 
    	IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type CardGetMethodFilterPolicy = 
        class
            interface IFilterPolicy
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetMethodFilterPolicy
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm), [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm)
##  __Конструкторы
[CardGetMethodFilterPolicy](M_Tessa_Cards_Extensions_CardGetMethodFilterPolicy__ctor.htm)|
Инициализирует новый экземпляр класса CardGetMethodFilterPolicy  
---|---  
##  __Свойства
[Instance](P_Tessa_Cards_Extensions_CardGetMethodFilterPolicy_Instance.htm)|
Экземпляр класса.  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[FilterAsync](M_Tessa_Cards_Extensions_CardGetMethodFilterPolicy_FilterAsync.htm)|
Возвращает признак того, что выполнение метода с заданным параметром разрешено
для экземпляра расширения.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetFilterContextAsync](M_Tessa_Cards_Extensions_CardGetMethodFilterPolicy_GetFilterContextAsync.htm)|
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
