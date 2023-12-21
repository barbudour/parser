# CardNewStrategy - класс
Стратегия создания карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardNewStrategy : ICardNewStrategy
VB __Копировать
     Public NotInheritable Class CardNewStrategy
    	Implements ICardNewStrategy
C++ __Копировать
     public ref class CardNewStrategy sealed : ICardNewStrategy
F# __Копировать
     [<SealedAttribute>]
    type CardNewStrategy = 
        class
            interface ICardNewStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardNewStrategy
Implements
    [ICardNewStrategy](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
##  __Конструкторы
[CardNewStrategy](M_Tessa_Cards_ComponentModel_CardNewStrategy__ctor.htm)|
Создаёт экземпляр объекта с указанием стратегии кэширования.  
---|---  
## __Свойства
[Default](P_Tessa_Cards_ComponentModel_CardNewStrategy_Default.htm)|
Стратегия по умолчанию, не выполняющая кэширование результатов.  
---|---  
## __Методы
[CreateResponseAsync](M_Tessa_Cards_ComponentModel_CardNewStrategy_CreateResponseAsync.htm)|
Создаёт ответ на запрос по созданию карточки, содержащий данные секций
карточки.  
---|---  
[CreateSectionRowsAsync](M_Tessa_Cards_ComponentModel_CardNewStrategy_CreateSectionRowsAsync.htm)|
Создаёт пустые строки коллекционных или древовидных секций создаваемой
карточки, доступные по имени секции.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FillEntryFieldsAsync](M_Tessa_Cards_ComponentModel_CardNewStrategy_FillEntryFieldsAsync.htm)|
Заполняет поля строковой секции в соответствии с заданной метаинформацией.  
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
[SetSessionInfoAsync](M_Tessa_Cards_ComponentModel_CardNewStrategy_SetSessionInfoAsync.htm)|
Устанавливает информацию о пользователе, создавшем карточку, по объекту
сессии.  
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
