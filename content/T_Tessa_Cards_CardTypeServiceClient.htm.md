# CardTypeServiceClient - класс
Сервис для управления типами карточек, доступный на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardTypeServiceClient : ICardTypeService
VB __Копировать
     Public NotInheritable Class CardTypeServiceClient
    	Implements ICardTypeService
C++ __Копировать
     public ref class CardTypeServiceClient sealed : ICardTypeService
F# __Копировать
     [<SealedAttribute>]
    type CardTypeServiceClient = 
        class
            interface ICardTypeService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardTypeServiceClient
Implements
    [ICardTypeService](T_Tessa_Cards_ICardTypeService.htm)
##  __Конструкторы
[CardTypeServiceClient](M_Tessa_Cards_CardTypeServiceClient__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
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
[GetAllCardTypesAsync](M_Tessa_Cards_CardTypeServiceClient_GetAllCardTypesAsync.htm)|
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.  
[GetCachedMetadataAsync](M_Tessa_Cards_CardTypeServiceClient_GetCachedMetadataAsync.htm)|
Возвращает метаинформацию, описывающую типы всех карточек, со всей необходимой
информацией. Возвращаемая метаинформация и содержащиеся в ней типы карточек
защищены от изменений.  
[GetCardTypeAsync](M_Tessa_Cards_CardTypeServiceClient_GetCardTypeAsync.htm)|
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
[StoreAsync](M_Tessa_Cards_CardTypeServiceClient_StoreAsync.htm)| Добавляет,
обновляет и удаляет типы карточек.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[DeleteAsync](M_Tessa_Cards_CardExtensions_DeleteAsync_2.htm)|  Удаляет
заданный тип карточки.  
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
