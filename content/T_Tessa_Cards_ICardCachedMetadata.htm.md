# ICardCachedMetadata - интерфейс
Содержит кэш метаинформации, которая необходима для использования типов
карточек совместно с пакетом карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardCachedMetadata : ICardMetadata, 
    	ISealable
VB __Копировать
     Public Interface ICardCachedMetadata
    	Inherits ICardMetadata, ISealable
C++ __Копировать
     public interface class ICardCachedMetadata : ICardMetadata, 
    	ISealable
F# __Копировать
     type ICardCachedMetadata = 
        interface
            interface ICardMetadata
            interface ISealable
        end
Implements
    [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[HasData](P_Tessa_Cards_ICardCachedMetadata_HasData.htm)|  Признак того, что
кэш содержит данные. Если значение равно false, то кэш ещё не заполнен или
сброшен, поэтому обращение к другим его свойствам приведёт к наполнению
метаинформации.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __Методы
[GetCachedMetadataAsync](M_Tessa_Cards_ICardCachedMetadata_GetCachedMetadataAsync.htm)|
Возвращает исходный объект метаинформации, который кэшируется текущим
объектом.  
---|---  
[GetCardTypesAsync](M_Tessa_Cards_ICardMetadata_GetCardTypesAsync.htm)|
Возвращает список типов карточек карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[GetDamagedCardTypeIDListAsync](M_Tessa_Cards_ICardMetadata_GetDamagedCardTypeIDListAsync.htm)|
Возвращает список идентификаторов повреждённых типов карточек. Собственно типы
карточек можно получить посредством сервиса типов карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[GetEnumerationsAsync](M_Tessa_Cards_ICardMetadata_GetEnumerationsAsync.htm)|
Возвращает список перечислений.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[GetGlobalReferencesAsync](M_Tessa_Cards_ICardMetadata_GetGlobalReferencesAsync.htm)|
Возвращает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl]), совместно использующиеся в типах карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[GetMetadataForTypeAsync](M_Tessa_Cards_ICardMetadata_GetMetadataForTypeAsync.htm)|
Возвращает выборку из метаинформации, которая относится только к заданному
типу карточек. В возвращённую выборку не передаются перечисления.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[GetSectionsAsync](M_Tessa_Cards_ICardMetadata_GetSectionsAsync.htm)|
Возвращает метаинформацию по секциям карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[GetValidationResultAsync](M_Tessa_Cards_ICardMetadata_GetValidationResultAsync.htm)|
Возвращает результат валидации при построении метаинформации.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[InvalidateAsync](M_Tessa_Cards_ICardCachedMetadata_InvalidateAsync.htm)|
Сбрасывает кэш метаинформации. При следующем обращении к содержимому
метаинформации будет выполнен запрос на получение её из сервиса типов
карточек.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SetAsync](M_Tessa_Cards_ICardCachedMetadata_SetAsync.htm)|  Устанавливает
заданную метаинформацию в кэше. При этом метаинформация защищается от
изменений, если кэш также защищён от изменений.  
[SetCardTypesAsync](M_Tessa_Cards_ICardMetadata_SetCardTypesAsync.htm)|
Устанавливает список типов карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[SetDamagedCardTypeIDListAsync](M_Tessa_Cards_ICardMetadata_SetDamagedCardTypeIDListAsync.htm)|
Устанавливает список идентификаторов повреждённых типов карточек. Собственно
типы карточек можно получить посредством сервиса типов карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[SetEnumerationsAsync](M_Tessa_Cards_ICardMetadata_SetEnumerationsAsync.htm)|
Устанавливает список перечислений.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[SetGlobalReferencesAsync](M_Tessa_Cards_ICardMetadata_SetGlobalReferencesAsync.htm)|
Устанавливает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl], [CardTypeValidator], [CardTypeExtension]), совместно
использующиеся в типах карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[SetSectionsAsync](M_Tessa_Cards_ICardMetadata_SetSectionsAsync.htm)|
Метаинформация по секциям карточек.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[SetValidationResultAsync](M_Tessa_Cards_ICardMetadata_SetValidationResultAsync.htm)|
Устанавливает результат валидации при построении метаинформации.  
(Унаследован от [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm))  
[UpdateAsync](M_Tessa_Cards_ICardCachedMetadata_UpdateAsync.htm)|  Обновляет
кэш метаинформации из сервиса типов карточек. Если объект защищён от изменений
посредством метода [Tessa.Platform.ISealable.Seal] и имеет доступ к объектам
метаинформации, переданным через конструктор, то выполняется более эффективный
запрос к серверу для получения актуальной метаинформации.  
## __Методы расширения
[GetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
---|---  
[GetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
