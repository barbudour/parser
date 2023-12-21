# CardTypeClientRepository - класс
Репозиторий для управления типами карточек на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardTypeClientRepository : ICardTypeClientRepository
VB __Копировать
     Public NotInheritable Class CardTypeClientRepository
    	Implements ICardTypeClientRepository
C++ __Копировать
     public ref class CardTypeClientRepository sealed : ICardTypeClientRepository
F# __Копировать
     [<SealedAttribute>]
    type CardTypeClientRepository = 
        class
            interface ICardTypeClientRepository
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardTypeClientRepository
Implements
    [ICardTypeClientRepository](T_Tessa_Cards_ICardTypeClientRepository.htm)
##  __Конструкторы
[CardTypeClientRepository](M_Tessa_Cards_CardTypeClientRepository__ctor.htm)|
Создаёт экземпляр класса с указанием сервиса типов карточек.  
---|---  
## __Методы
[DeleteAsync](M_Tessa_Cards_CardTypeClientRepository_DeleteAsync.htm)| Удаляет
тип карточки с заданным идентификатором.  
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
[GetAllCardTypesAsync](M_Tessa_Cards_CardTypeClientRepository_GetAllCardTypesAsync.htm)|
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.  
[GetCachedMetadataAsync](M_Tessa_Cards_CardTypeClientRepository_GetCachedMetadataAsync.htm)|
Возвращает метаинформацию, описывающую типы всех карточек, со всей необходимой
информацией. Возвращаемая метаинформация и содержащиеся в ней типы карточек
защищены от изменений.  
[GetCardTypeAsync](M_Tessa_Cards_CardTypeClientRepository_GetCardTypeAsync.htm)|
Возвращает объект, описывающий тип карточки, со всей необходимой информацией.  
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
[StoreAsync](M_Tessa_Cards_CardTypeClientRepository_StoreAsync.htm)| Добавляет
или обновляет тип карточки.  
[StoreManyAsync](M_Tessa_Cards_CardTypeClientRepository_StoreManyAsync.htm)|
Добавляет, обновляет и удаляет типы карточек.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[DeleteAsync](M_Tessa_Cards_CardExtensions_DeleteAsync.htm)|  Удаляет заданный
тип карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
