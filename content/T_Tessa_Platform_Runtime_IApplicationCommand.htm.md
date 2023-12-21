# IApplicationCommand - интерфейс
Команда, выполняемая при запуске приложения. Обычно связана с аргументами
командной строки.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationCommand
VB __Копировать
     Public Interface IApplicationCommand
C++ __Копировать
     public interface class IApplicationCommand
F# __Копировать
     type IApplicationCommand = interface end
##  __Свойства
[Command](P_Tessa_Platform_Runtime_IApplicationCommand_Command.htm)|
Выполняемая команда. Обычно это одна из констант в классе
[Tessa.Platform.Runtime.ApplicationCommandTypes]. Не может быть равна null или
пустой строке.  
---|---  
[Info](P_Tessa_Platform_Runtime_IApplicationCommand_Info.htm)| Дополнительная
информация, ассоциированная с командой.  
[Parameter](P_Tessa_Platform_Runtime_IApplicationCommand_Parameter.htm)|
Параметр команды. Может быть равен null или пустой строке, если параметр
отсутствует.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
