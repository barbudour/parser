# CardHelper.CompressFileVersions - метод
Выполняет упаковку запроса на получение информации по версиям файла. Заданный
декоратор становится непригоден к использованию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Dictionary<string, Object> CompressFileVersions(
    	CardGetFileVersionsResponse response
    )
VB __Копировать
     Public Shared Function CompressFileVersions ( 
    	response As CardGetFileVersionsResponse
    ) As Dictionary(Of String, Object)
C++ __Копировать
     public:
    static Dictionary<String^, Object^>^ CompressFileVersions(
    	CardGetFileVersionsResponse^ response
    )
F# __Копировать
     static member CompressFileVersions : 
            response : CardGetFileVersionsResponse -> Dictionary<string, Object> 
#### Параметры
response
[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm)
    Ответ на запрос по получению информации по версиям файла, прикреплённого к карточке, от сервиса карточек.
#### Возвращаемое значение
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Хранилище, содержащее упакованные данные запроса на получение информации по
версиям файла. Такие данные несовместимы с декораторами.
##  __Заметки
Для распаковки пакета карточки можно использовать метод
[DecompressFileVersions(IStorageObjectProvider)](M_Tessa_Cards_CardHelper_DecompressFileVersions_1.htm).
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
