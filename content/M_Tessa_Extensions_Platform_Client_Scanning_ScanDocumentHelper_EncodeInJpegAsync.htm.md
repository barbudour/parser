# ScanDocumentHelper.EncodeInJpegAsync(Stream, String, Int32) - метод
Выполняет кодирование изображения любого допустимого формата из потока
sourceStream в формат JPEG, совместимый с PDF.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask EncodeInJpegAsync(
    	Stream sourceStream,
    	string targetName,
    	int qualityPercentage = 50
    )
VB __Копировать
     Public Shared Function EncodeInJpegAsync ( 
    	sourceStream As Stream,
    	targetName As String,
    	Optional qualityPercentage As Integer = 50
    ) As ValueTask
C++ __Копировать
     public:
    static ValueTask EncodeInJpegAsync(
    	Stream^ sourceStream, 
    	String^ targetName, 
    	int qualityPercentage = 50
    )
F# __Копировать
     static member EncodeInJpegAsync : 
            sourceStream : Stream * 
            targetName : string * 
            ?qualityPercentage : int 
    (* Defaults:
            let _qualityPercentage = defaultArg qualityPercentage 50
    *)
    -> ValueTask 
#### Параметры
sourceStream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток с конвертируемым изображением.
targetName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к результату конвертации в файле JPEG.
qualityPercentage [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
    Процент качества кодирования в JPEG. Рекомендуется использовать значение по умолчанию.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[ScanDocumentHelper -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper.htm)
[EncodeInJpegAsync -
перегрузка](Overload_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_EncodeInJpegAsync.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
