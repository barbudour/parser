# ICardMetadataExtensionContext - интерфейс
Контекст расширения, выполняемого при построении метаинформации по типам
карточек [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardMetadataExtensionContext : ITraceableExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public Interface ICardMetadataExtensionContext
    	Inherits ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public interface class ICardMetadataExtensionContext : ITraceableExtensionContext, 
    	IExtensionContext
F# __Копировать
     type ICardMetadataExtensionContext = 
        interface
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[CardMetadata](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_CardMetadata.htm)|
Построенная метаинформация по типам карточек, которую расширение может
изменять, или null, если расширение вызвано на этапе, на котором
метаинформация ещё не построена.  
[CardTypes](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_CardTypes.htm)|
Типы карточек, используемые для построения метаинформации.  
[DelayedSchemeCheckCardTypeIDSet](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_DelayedSchemeCheckCardTypeIDSet.htm)|
Идентификаторы типов карточек, проверка схемы для которых выполняется после
выполнения всех расширений на метаинформацию.
Рекомендуется добавить идентификатор типа карточки в методе расширения
[ModifyTypes(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyTypes.htm),
чтобы позже в методе расширения
[ModifyMetadata(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyMetadata.htm)
добавить секции и колонки, отсутствующие в схеме данных.
Если по завершении этого метода в типе карточки cardType.SchemeItems
присутствуют ссылки на секции или колонки, отсутствующие в секциях
cardMetadata.GetSectionsAsync(), то тип считается повреждённым, и добавляется
такое же сообщение об ошибке, как если бы проверка типа не была отложена.  
[EnableTracing](P_Tessa_Extensions_ITraceableExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
[GlobalReferences](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_GlobalReferences.htm)|
Словарь, содержащий глобальные объекты
([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm),
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm),
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm),
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm),
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)), совместно
использующиеся в типах карточек.  
[Info](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_Info.htm)|
Информация, используемая для передачи между расширениями в цепочке.  
[SchemeService](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_SchemeService.htm)|
Объект, обеспечивающий доступ к схеме данных.  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
