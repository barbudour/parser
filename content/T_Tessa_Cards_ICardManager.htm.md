# ICardManager - интерфейс
Объект, управляющий операциями с карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardManager
VB __Копировать
     Public Interface ICardManager
C++ __Копировать
     public interface class ICardManager
F# __Копировать
     type ICardManager = interface end
##  __Методы
[CreateFromTemplateAsync(ISourceContentProvider,
Func<CardFileContentParameter, ValueTask>, Dictionary<String, Object>,
CardFileFormat,
CancellationToken)](M_Tessa_Cards_ICardManager_CreateFromTemplateAsync_1.htm)|
Создаёт карточку по шаблону.  
---|---  
[CreateFromTemplateAsync(CardStoreRequest, CardHeader, Func<Int64,
CancellationToken, ValueTask<SubStream>>, Func<CardFileContentParameter,
ValueTask>, Dictionary<String, Object>, ICardFileSourceMapping,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ICardManager_CreateFromTemplateAsync.htm)|
Создаёт карточку по шаблону.  
[ExportAsync(CardGetRequest, CardFileFormat,
CancellationToken)](M_Tessa_Cards_ICardManager_ExportAsync.htm)|  Выполняет
административный экспорт карточки с файлами и заданиями, но не загружает
контент файлов.  
[ExportAsync(CardGetRequest, ISourceContentProvider, Dictionary<String,
Object>, CardFileFormat, IReadOnlyCollection<IStorageContentMapping>, Boolean,
CancellationToken)](M_Tessa_Cards_ICardManager_ExportAsync_1.htm)|  Выполняет
административный экспорт карточки со всем её содержимым, включая файлы и
задания.  
[GetExportedCardAsync](M_Tessa_Cards_ICardManager_GetExportedCardAsync.htm)|
Загружает карточку, которая была экспортирована в файл.  
[ImportAsync(ISourceContentProvider, Dictionary<String, Object>,
CardFileFormat, Card, ICardMergeOptions, ILogger, Func<String, Boolean>,
Boolean, CancellationToken)](M_Tessa_Cards_ICardManager_ImportAsync_1.htm)|
Выполняет административный импорт карточки со всем её содержимым, включая
файлы и задания.  
[ImportAsync(CardStoreRequest, CardHeader,
IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>>,
Dictionary<String, Object>, CardFileFormat, Card, ICardMergeOptions, ILogger,
Boolean, CancellationToken)](M_Tessa_Cards_ICardManager_ImportAsync.htm)|
Выполняет административный импорт карточки со всем её содержимым, включая
файлы и задания.  
[PrepareCardInTemplateForEditingAsync](M_Tessa_Cards_ICardManager_PrepareCardInTemplateForEditingAsync.htm)|
Подготавливает карточку в шаблоне, десериализованную из шаблона, к
редактированию.  
[PrepareCardInTemplateForStoringAsync](M_Tessa_Cards_ICardManager_PrepareCardInTemplateForStoringAsync.htm)|
Подготавливает отредактированную карточку в шаблоне для сериализации и
сохранения в шаблоне.  
[ReadExportedRequestAsync](M_Tessa_Cards_ICardManager_ReadExportedRequestAsync.htm)|
Выполняет чтение запроса на импорт карточки из потока, содержащего
экспортированную карточку.  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
