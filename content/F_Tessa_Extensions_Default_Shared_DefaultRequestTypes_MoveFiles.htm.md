# DefaultRequestTypes.MoveFiles - поле
Запрос на перенос контента файла на заданный источник
[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm). Рекомендуется
вызывать запрос методом [MoveFilesToAsync(CardFileSourceType, ICardRepository,
Guid, Nullable<Guid>,
CancellationToken)](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_MoveFilesToAsync.htm).
В запросе должен быть указан идентификатор карточки
[CardID](P_Tessa_Cards_CardRequest_CardID.htm) и источник
[SetSourceID(CardRequest,
CardFileSourceType)](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_SetSourceID.htm).
Если также указан идентификатор файла
[FileID](P_Tessa_Cards_CardRequest_FileID.htm), то переносятся только все
версии заданного файла, иначе - все версии всех файлов карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly Guid MoveFiles
VB __Копировать
     Public Shared ReadOnly MoveFiles As Guid
C++ __Копировать
     public:
    static initonly Guid MoveFiles
F# __Копировать
     static val MoveFiles: Guid
#### Значение поля
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
##  __См. также
#### Ссылки
[DefaultRequestTypes -
](T_Tessa_Extensions_Default_Shared_DefaultRequestTypes.htm)
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
