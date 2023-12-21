# CardTaskDialogHelper - класс
Содержит вспомогательные методы для работы с диалогами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardTaskDialogHelper
VB __Копировать
     Public NotInheritable Class CardTaskDialogHelper
C++ __Копировать
     public ref class CardTaskDialogHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardTaskDialogHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardTaskDialogHelper
##  __Методы
[ClearDialogFiles](M_Tessa_Cards_CardTaskDialogHelper_ClearDialogFiles.htm)|
Удаляет файлы из основной карточки, которые были добавлены из карточки
диалога.  
---|---  
[GetAllCompletionOptionSettings](M_Tessa_Cards_CardTaskDialogHelper_GetAllCompletionOptionSettings.htm)|
Возвращает коллекцию содержащую информацию по всем параметрам диалога
содержащиеся в заданном задании.  
[GetCardTaskDialogActionResult(CardInfoStorageObject)](M_Tessa_Cards_CardTaskDialogHelper_GetCardTaskDialogActionResult_1.htm)|
Возвращает информацию о завершении диалога.  
[GetCardTaskDialogActionResult(IDictionary<String,
Object>)](M_Tessa_Cards_CardTaskDialogHelper_GetCardTaskDialogActionResult.htm)|
Возвращает информацию о завершении диалога.  
[GetCompletionOptionSettings(CardTask,
Guid)](M_Tessa_Cards_CardTaskDialogHelper_GetCompletionOptionSettings_1.htm)|
Возвращает параметры диалога имеющие указанный идентификатор.  
[GetCompletionOptionSettings(IDictionary<String, Object>,
Guid)](M_Tessa_Cards_CardTaskDialogHelper_GetCompletionOptionSettings.htm)|
Возвращает параметры диалога имеющие указанный идентификатор.  
[GetDialogCardAsync](M_Tessa_Cards_CardTaskDialogHelper_GetDialogCardAsync.htm)|
Возвращает карточку диалога.  
[GetFileContentFromBase64Async](M_Tessa_Cards_CardTaskDialogHelper_GetFileContentFromBase64Async.htm)|
Возвращает массив байт содержащий контент файла указанный в виде строки в
Base64.  
[GetFileContentFromInfo](M_Tessa_Cards_CardTaskDialogHelper_GetFileContentFromInfo.htm)|
Возвращает контент файла диалога с временем жизни "Запрос"
([Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm)) представленный в виде
строки в Base64.  
[GetFileContentStreamFromBase64Async](M_Tessa_Cards_CardTaskDialogHelper_GetFileContentStreamFromBase64Async.htm)|
Возвращает поток содержащий контент файла указанный в виде строки в Base64.  
[GetFileVersionFromInfo](M_Tessa_Cards_CardTaskDialogHelper_GetFileVersionFromInfo.htm)|
Возвращает информацию о версии файла диалога с временем жизни "Запрос"
([Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm)).  
[PrepareDialogCardToSave](M_Tessa_Cards_CardTaskDialogHelper_PrepareDialogCardToSave.htm)|
Подготавливает карточку диалога с временем жизни
[Settings](T_Tessa_Cards_CardTaskDialogStoreMode.htm) или
[Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm) к сохранению.  
[PrepareFilesInSettingsDialogCardForStore](M_Tessa_Cards_CardTaskDialogHelper_PrepareFilesInSettingsDialogCardForStore.htm)|
Подготавливает файлы карточки диалога с временем жизни
[Settings](T_Tessa_Cards_CardTaskDialogStoreMode.htm) к сохранению.  
[SetCardTaskDialogActionResult(CardInfoStorageObject,
CardTaskDialogActionResult)](M_Tessa_Cards_CardTaskDialogHelper_SetCardTaskDialogActionResult_1.htm)|
Задаёт информацию о завершении диалога.  
[SetCardTaskDialogActionResult(CardTask,
CardTaskDialogActionResult)](M_Tessa_Cards_CardTaskDialogHelper_SetCardTaskDialogActionResult_2.htm)|
Задаёт информацию о завершении диалога.  
[SetCardTaskDialogActionResult(IDictionary<String, Object>,
CardTaskDialogActionResult)](M_Tessa_Cards_CardTaskDialogHelper_SetCardTaskDialogActionResult.htm)|
Задаёт информацию о завершении диалога.  
[SetCompletionOptionSettings](M_Tessa_Cards_CardTaskDialogHelper_SetCompletionOptionSettings.htm)|
Устанавливает параметры диалога в настройках указанного задания.  
[SetFileContentToInfo(CardFile, Byte[],
IUser)](M_Tessa_Cards_CardTaskDialogHelper_SetFileContentToInfo.htm)|  Задаёт
контент файла карточки диалога с временем жизни
[Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm).  
[SetFileContentToInfo(CardInfoStorageObject, String,
CardFileVersion)](M_Tessa_Cards_CardTaskDialogHelper_SetFileContentToInfo_1.htm)|
Задаёт информацию о файле диалога с временем жизни "Запрос"
([Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm)).  
[SetFileContentToInfoAsync](M_Tessa_Cards_CardTaskDialogHelper_SetFileContentToInfoAsync.htm)|
Асинхронно задаёт контент указанных файлов в соответствующие [!:CardFile.Info]
карточки файлов.  
[SetFileContentToMainCard](M_Tessa_Cards_CardTaskDialogHelper_SetFileContentToMainCard.htm)|
Задаёт контент указанных файлов в основную карточку.  
## __Поля
[CompleteOption](F_Tessa_Cards_CardTaskDialogHelper_CompleteOption.htm)|
Вариант завершения "Завершить".  
---|---  
[DialogFileKey](F_Tessa_Cards_CardTaskDialogHelper_DialogFileKey.htm)|  Ключ,
по которому в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) объекта
[CardFile](T_Tessa_Cards_CardFile.htm), содержится значение, показывающее, что
файл относится к диалогу. Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
[ShowDialogOption](F_Tessa_Cards_CardTaskDialogHelper_ShowDialogOption.htm)|
Вариант завершения "Показать диалог".  
[StoreMode](F_Tessa_Cards_CardTaskDialogHelper_StoreMode.htm)|  Ключ, по
которому в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) запроса на
создание [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm) или получение
[CardGetRequest](T_Tessa_Cards_CardGetRequest.htm) карточки содержится режим
сохранения карточки диалога. Тип значения:
[CardTaskDialogStoreMode](T_Tessa_Cards_CardTaskDialogStoreMode.htm)
представленное в виде значения базового типа.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
