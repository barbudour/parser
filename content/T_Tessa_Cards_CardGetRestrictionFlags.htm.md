# CardGetRestrictionFlags - перечисление
Флаги, ограничивающие загружаемую по карточке информацию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum CardGetRestrictionFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration CardGetRestrictionFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class CardGetRestrictionFlags
F# __Копировать
     [<FlagsAttribute>]
    type CardGetRestrictionFlags
##  __Члены
None| 0|  Флаги не заданы, т.е. карточка загружается полностью.  
---|---|---  
RestrictSections| 1|  Не загружаются данные секций карточки. Если флаг
установлен и карточка загружается для редактирования, то пустые строки для
коллекционных и древовидных секций также не будут установлены. Этот флаг не
учитывает загрузку секций файлов и заданий.  
RestrictFiles| 2|  Не загружаются файлы карточки.  
RestrictFileSections| 4|  Не загружаются секции файлов карточки. Если
установлен флаг RestrictFiles, то этот флаг игнорируется.  
RestrictTasks| 8|  Не загружаются задания карточки. Задания по умолчанию
загружаются для всех карточек, в типе которых установлен флаг
[AllowTasks](T_Tessa_Cards_CardTypeFlags.htm).  
RestrictTaskSections| 16|  Не загружаются секции заданий карточки. Если
установлен флаг RestrictTasks, то этот флаг игнорируется.  
RestrictTaskCalendar| 32|  Не загружается информация из календаря при загрузке
заданий. К такой информации относится время, оставшееся до завершения задания.
Если установлен флаг RestrictTasks, то этот флаг игнорируется.  
RestrictTaskHistory| 64|  Не загружается информация по истории заданий.
История заданий по умолчанию загружается для всех карточек, в типе которых
установлен флаг [AllowTasks](T_Tessa_Cards_CardTypeFlags.htm). Поведение флага
не зависит от других ограничивающих флагов, в т.ч. от флага RestrictTasks.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
