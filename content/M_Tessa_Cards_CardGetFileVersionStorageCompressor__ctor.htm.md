# CardGetFileVersionStorageCompressor - конструктор
Создаёт экземпляр класса с указанием объектов, используемых для упаковки и
распаковки версий файлов карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetFileVersionStorageCompressor(
    	IStorageCompressor fileVersionCompressor = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional fileVersionCompressor As IStorageCompressor = Nothing
    )
C++ __Копировать
     public:
    CardGetFileVersionStorageCompressor(
    	IStorageCompressor^ fileVersionCompressor = nullptr
    )
F# __Копировать
     new : 
            ?fileVersionCompressor : IStorageCompressor 
    (* Defaults:
            let _fileVersionCompressor = defaultArg fileVersionCompressor null
    *)
    -> CardGetFileVersionStorageCompressor
#### Параметры
fileVersionCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
    Объект, используемый для упаковки и распаковки версий файлов карточки.
##  __См. также
#### Ссылки
[CardGetFileVersionStorageCompressor -
](T_Tessa_Cards_CardGetFileVersionStorageCompressor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
