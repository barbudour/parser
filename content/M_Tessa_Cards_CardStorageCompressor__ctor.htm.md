# CardStorageCompressor - конструктор
Создаёт экземпляр класса с указанием объектов, используемых для упаковки и
распаковки карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStorageCompressor(
    	IStorageCompressor sectionCompressor = null,
    	IStorageCompressor fileCompressor = null,
    	IStorageCompressor fileVersionCompressor = null,
    	IStorageCompressor taskCompressor = null,
    	IStorageCompressor taskHistoryCompressor = null,
    	IStorageCompressor taskHistoryGroupsCompressor = null,
    	IStorageCompressor topicsCompressor = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional sectionCompressor As IStorageCompressor = Nothing,
    	Optional fileCompressor As IStorageCompressor = Nothing,
    	Optional fileVersionCompressor As IStorageCompressor = Nothing,
    	Optional taskCompressor As IStorageCompressor = Nothing,
    	Optional taskHistoryCompressor As IStorageCompressor = Nothing,
    	Optional taskHistoryGroupsCompressor As IStorageCompressor = Nothing,
    	Optional topicsCompressor As IStorageCompressor = Nothing
    )
C++ __Копировать
     public:
    CardStorageCompressor(
    	IStorageCompressor^ sectionCompressor = nullptr, 
    	IStorageCompressor^ fileCompressor = nullptr, 
    	IStorageCompressor^ fileVersionCompressor = nullptr, 
    	IStorageCompressor^ taskCompressor = nullptr, 
    	IStorageCompressor^ taskHistoryCompressor = nullptr, 
    	IStorageCompressor^ taskHistoryGroupsCompressor = nullptr, 
    	IStorageCompressor^ topicsCompressor = nullptr
    )
F# __Копировать
     new : 
            ?sectionCompressor : IStorageCompressor * 
            ?fileCompressor : IStorageCompressor * 
            ?fileVersionCompressor : IStorageCompressor * 
            ?taskCompressor : IStorageCompressor * 
            ?taskHistoryCompressor : IStorageCompressor * 
            ?taskHistoryGroupsCompressor : IStorageCompressor * 
            ?topicsCompressor : IStorageCompressor 
    (* Defaults:
            let _sectionCompressor = defaultArg sectionCompressor null
            let _fileCompressor = defaultArg fileCompressor null
            let _fileVersionCompressor = defaultArg fileVersionCompressor null
            let _taskCompressor = defaultArg taskCompressor null
            let _taskHistoryCompressor = defaultArg taskHistoryCompressor null
            let _taskHistoryGroupsCompressor = defaultArg taskHistoryGroupsCompressor null
            let _topicsCompressor = defaultArg topicsCompressor null
    *)
    -> CardStorageCompressor
#### Параметры
sectionCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
     Объект, используемый для упаковки и распаковки секций карточки и секций вложенных в карточку файлов. 
fileCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
    Объект, используемый для упаковки и распаковки файлов карточки.
fileVersionCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
    Объект, используемый для упаковки и распаковки версий файлов карточки.
taskCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
    Объект, используемый для упаковки и распаковки заданий карточки.
taskHistoryCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
    Объект, используемый для упаковки и распаковки истории заданий карточки.
taskHistoryGroupsCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
    Объект, используемый для упаковки и распаковки групп истории заданий карточки.
topicsCompressor
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
(Optional)
    Объект, используемый для упаковки и распаковки топиков карточки.
##  __См. также
#### Ссылки
[CardStorageCompressor - ](T_Tessa_Cards_CardStorageCompressor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
