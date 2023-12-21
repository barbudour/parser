# CardHelper.DecompressFileVersions(IStorageObjectProvider) - метод
Выполняет распаковку запроса на получение информации по версиям файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardGetFileVersionsResponse DecompressFileVersions(
    	IStorageObjectProvider storageObjectProvider
    )
VB __Копировать
     Public Shared Function DecompressFileVersions ( 
    	storageObjectProvider As IStorageObjectProvider
    ) As CardGetFileVersionsResponse
C++ __Копировать
     public:
    static CardGetFileVersionsResponse^ DecompressFileVersions(
    	IStorageObjectProvider^ storageObjectProvider
    )
F# __Копировать
     static member DecompressFileVersions : 
            storageObjectProvider : IStorageObjectProvider -> CardGetFileVersionsResponse 
#### Параметры
storageObjectProvider
[IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm)
     Объект, предоставляющий доступ к хранилищу, содержащему упакованные данные запроса на получение информации по версиям файла. 
#### Возвращаемое значение
[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm)  
Декоратор для запроса на получение информации по версиям файла, полученный в
результате распаковки.
##  __Заметки
Для упаковки запроса на получение информации по версиям файла можно
использовать метод
[CompressFileVersions(CardGetFileVersionsResponse)](M_Tessa_Cards_CardHelper_CompressFileVersions.htm).
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[DecompressFileVersions -
перегрузка](Overload_Tessa_Cards_CardHelper_DecompressFileVersions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
