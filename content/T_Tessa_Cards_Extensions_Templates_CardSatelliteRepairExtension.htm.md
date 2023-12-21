# CardSatelliteRepairExtension - класс
Шаблон расширения для исправления структуры карточки-сателлита.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardSatelliteRepairExtension : CardRepairExtension
VB __Копировать
     Public MustInherit Class CardSatelliteRepairExtension
    	Inherits CardRepairExtension
C++ __Копировать
     public ref class CardSatelliteRepairExtension abstract : public CardRepairExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardSatelliteRepairExtension = 
        class
            inherit CardRepairExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm) __ CardSatelliteRepairExtension
##  __Конструкторы
[CardSatelliteRepairExtension](M_Tessa_Cards_Extensions_Templates_CardSatelliteRepairExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardSatelliteRepairExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_Templates_CardSatelliteRepairExtension_AfterRequest.htm)|
Действие, выполняемое после исправления структуры карточки как при успешном,
так и при неудачном результате.  
(Переопределяет
[CardRepairExtension.AfterRequest(ICardRepairExtensionContext)](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после исправления
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardRepairExtension_BeforeRequest.htm)|
Действие, выполняемое перед исправлением структуры карточки.  
(Унаследован от
[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm))  
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
[IsMainCardTypeAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteRepairExtension_IsMainCardTypeAsync.htm)|
Возвращает признак того, что заданный тип карточки является допустимым типом
основной карточки.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetSatelliteCardAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteRepairExtension_TryGetSatelliteCardAsync.htm)|
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.  
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
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
