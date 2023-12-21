# FileSpecialFolder - перечисление
Тип специальной папки, используемой в системе.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum FileSpecialFolder
VB __Копировать
     Public Enumeration FileSpecialFolder
C++ __Копировать
     public enum class FileSpecialFolder
F# __Копировать
     type FileSpecialFolder
##  __Члены
Temp| 0|  Временная папка для хранения файлов. Обычно располагается во
временной папке Windows или Linux.  
---|---|---  
TempBase| 1|  Временная папка, внутри которой можно создать подпапку для
хранения любых данных. Не рекомендуется записывать прямо в ту папку, которая
возвращается этим методом. Обычно располагается во временной папке Windows или
Linux.  
Dumps| 2|  Папка с дампами ошибок. Например, с дампами редактора схемы данных.
Обычно располагается в папке %appdata% для Windows или Linux. Для Linux
%appdata% соответствует пути $HOMEDIR/.config.  
Data| 3|  Папка для хранения данных, например, для прикладываемых к письмам
файлов. Гарантированно не располагается во временной папке Windows или Linux.
Обычно располагается в папке %appdata%. Для Linux %appdata% соответствует пути
$HOMEDIR/.config.  
Sync| 4|  Папка с файлами синхронизации между процессами, в т.ч. с файлами
блокировок. Обычно располагается в папке %appdata%. Для Linux %appdata%
соответствует пути $HOMEDIR/.config.  
## __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
