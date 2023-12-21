# KrEventFlags - перечисление
Флаги, указывающие события, которые происходят с карточкой в типовом процессе.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Settings](N_Tessa_Extensions_Default_Shared_Settings.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum KrEventFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration KrEventFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class KrEventFlags
F# __Копировать
     [<FlagsAttribute>]
    type KrEventFlags
##  __Члены
None| 0|  События не указаны.  
---|---|---  
Register| 1|  Регистрация документа.  
Deregister| 2|  Дерегистрация документа.  
StartApproval| 4|  Запуск согласования.  
RebuildApproval| 8|  Возврат документа на доработку.  
RevokeApproval| 16|  Отзыв согласования.  
CancelApproval| 32|  Отмена согласования.  
All| 63|  Все поддерживаемые события, которые происходят с карточкой в типовом
процессе.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
