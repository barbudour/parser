# CardGlobalComponentCache - класс
Глобальный кэш для компонентов API карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardGlobalComponentCache : ICardGlobalComponentCache
VB __Копировать
     Public NotInheritable Class CardGlobalComponentCache
    	Implements ICardGlobalComponentCache
C++ __Копировать
     public ref class CardGlobalComponentCache sealed : ICardGlobalComponentCache
F# __Копировать
     [<SealedAttribute>]
    type CardGlobalComponentCache = 
        class
            interface ICardGlobalComponentCache
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGlobalComponentCache
Implements
    [ICardGlobalComponentCache](T_Tessa_Cards_ComponentModel_ICardGlobalComponentCache.htm)
##  __Конструкторы
[CardGlobalComponentCache](M_Tessa_Cards_ComponentModel_CardGlobalComponentCache__ctor.htm)|
Инициализирует новый экземпляр класса CardGlobalComponentCache  
---|---  
##  __Свойства
[LoadersByTypeID](P_Tessa_Cards_ComponentModel_CardGlobalComponentCache_LoadersByTypeID.htm)|
Объекты, загружающие карточку. Доступны по идентификаторам типов карточек.  
---|---  
[NewDefaultResponsesByTypeID](P_Tessa_Cards_ComponentModel_CardGlobalComponentCache_NewDefaultResponsesByTypeID.htm)|
Ответы на запросы, создающие структуру карточки для режима
[Tessa.Cards.CardNewMode.Default]. Доступны по идентификаторам типов карточек.  
[NewValidResponsesByTypeID](P_Tessa_Cards_ComponentModel_CardGlobalComponentCache_NewValidResponsesByTypeID.htm)|
Ответы на запросы, создающие структуру карточки для режима
[Tessa.Cards.CardNewMode.Valid]. Доступны по идентификаторам типов карточек.  
[SectionRowRemoverBySectionID](P_Tessa_Cards_ComponentModel_CardGlobalComponentCache_SectionRowRemoverBySectionID.htm)|
Объекты, содержащие информацию по удалению строк. Доступны по идентификаторам
секций карточек.  
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
[Invalidate](M_Tessa_Cards_ComponentModel_CardGlobalComponentCache_Invalidate.htm)|
Сбрасывает весь кэш.  
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
