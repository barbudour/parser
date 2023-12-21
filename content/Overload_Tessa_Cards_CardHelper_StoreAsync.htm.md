# CardHelper.StoreAsync - метод
##  __Список перегрузок
[StoreAsync(CardStoreRequest, IFileContainer, ICardRepository,
ICardStreamServerRepository,
CancellationToken)](M_Tessa_Cards_CardHelper_StoreAsync_1.htm)|  Выполняет
сохранение карточки на сервере с возможным наличием файлов. Не выполняет
проверку на наличие изменений в контенте файлов методом
[EnsureAllContentModifiedAsync(IEnumerable<IFile>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureAllContentModifiedAsync.htm).
Метод для внутреннего использования, рекомендуется использовать объект
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm) для сохранения карточки
с файлами, обратитесь к руководству разработчика за примерами.  
---|---  
[StoreAsync(CardStoreRequest, IFileContainer, ICardRepository,
ICardStreamClientRepository, Func<Double, CancellationToken, ValueTask>,
Int32, CancellationToken)](M_Tessa_Cards_CardHelper_StoreAsync.htm)|
Выполняет асинхронное сохранение карточки на клиенте с возможным наличием
файлов. Не выполняет проверку на наличие изменений в контенте файлов. Метод
для внутреннего использования, рекомендуется использовать объект
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm) для сохранения карточки
с файлами, обратитесь к руководству разработчика за примерами.  
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
