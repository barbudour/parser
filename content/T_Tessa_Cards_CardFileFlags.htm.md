# CardFileFlags - перечисление
Флаги файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum CardFileFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration CardFileFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class CardFileFlags
F# __Копировать
     [<FlagsAttribute>]
    type CardFileFlags
##  __Члены
None| 0|  Флаги отсутствуют.  
---|---|---  
UpdateName| 1|  Признак того, что при изменении файла следует также обновить
его имя [Name](P_Tessa_Cards_CardFile_Name.htm). Флаг учитывается только в том
случае, если выполняется сохранение карточки с файлом, у которого состояние
[State](P_Tessa_Cards_CardFile_State.htm) равно
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm). Состояние файла
автоматически устанавливается равным
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm), если флаг был
установлен перед сохранением на клиенте или если был явно вызван метод
[UpdateState()](M_Tessa_Cards_CardFile_UpdateState.htm). Флаг не
устанавливается при загрузке файла.  
UpdateCategory| 4|  Признак того, что при изменении файла следует также
обновить его категорию [CategoryID](P_Tessa_Cards_CardFile_CategoryID.htm).
Флаг учитывается только в том случае, если выполняется сохранение карточки с
файлом, у которого состояние [State](P_Tessa_Cards_CardFile_State.htm) равно
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm). Состояние файла
автоматически устанавливается равным
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm), если флаг был
установлен перед сохранением на клиенте или если был явно вызван метод
[UpdateState()](M_Tessa_Cards_CardFile_UpdateState.htm). Флаг не
устанавливается при загрузке файла.  
UpdateOrigin| 8|  Признак того, что при изменении файла следует также обновить
его исходный файл [OriginalFileID](P_Tessa_Cards_CardFile_OriginalFileID.htm),
из которого был скопирован этот файл. Флаг учитывается только в том случае,
если выполняется сохранение карточки с файлом, у которого состояние
[State](P_Tessa_Cards_CardFile_State.htm) равно
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm). Состояние файла
автоматически устанавливается равным
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm), если флаг был
установлен перед сохранением на клиенте или если был явно вызван метод
[UpdateState()](M_Tessa_Cards_CardFile_UpdateState.htm). Флаг не
устанавливается при загрузке файла.  
UpdateTask| 16|  Признак того, что при изменении файла следует также обновить
его ссылку на задание [TaskID](P_Tessa_Cards_CardFile_TaskID.htm). Это
позволяет перемещать файл между различными заданиями, а также между заданием и
карточкой. Флаг учитывается только в том случае, если выполняется сохранение
карточки с файлом, у которого состояние
[State](P_Tessa_Cards_CardFile_State.htm) равно
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm). Состояние файла
автоматически устанавливается равным
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm), если флаг был
установлен перед сохранением на клиенте или если был явно вызван метод
[UpdateState()](M_Tessa_Cards_CardFile_UpdateState.htm). Флаг не
устанавливается при загрузке файла.  
UpdateOptions| 32|  Признак того, что при изменении файла следует также
обновить его опции [Options](P_Tessa_Cards_CardFile_Options.htm). Флаг
учитывается только в том случае, если выполняется сохранение карточки с
файлом, у которого состояние [State](P_Tessa_Cards_CardFile_State.htm) равно
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm). Состояние файла
автоматически устанавливается равным
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm), если флаг был
установлен перед сохранением на клиенте или если был явно вызван метод
[UpdateState()](M_Tessa_Cards_CardFile_UpdateState.htm). Флаг не
устанавливается при загрузке файла.  
CalculateHash| 64|  Признак того, что для добавляемого файла или файла с
изменяющимся содержимым требуется рассчитать хеш-сумму
[Hash](P_Tessa_Cards_CardFile_Hash.htm) по фактически сохраняемому содержимому
файла, если она ещё не рассчитана. Флаг учитывается только в том случае, если
выполняется сохранение карточки с файлом, у которого состояние
[State](P_Tessa_Cards_CardFile_State.htm) равно
[Inserted](T_Tessa_Cards_CardFileState.htm),
[Replaced](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm) \- эти состояния можно
проверить вызовом file.State.HasContent(). Состояние файла не изменяется при
вызове метода [UpdateState()](M_Tessa_Cards_CardFile_UpdateState.htm) при
наличии этого флага. Флаг не устанавливается при загрузке файла.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
