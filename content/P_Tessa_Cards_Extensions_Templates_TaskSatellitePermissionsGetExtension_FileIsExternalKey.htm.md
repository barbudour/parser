# TaskSatellitePermissionsGetExtension.FileIsExternalKey - свойство
Имя уникального ключа, по которому в информации по файлу сателлита file.Info
будет указан признак того, что файл виртуальный и на самом деле относится к
основной карточке. Если в файле ключ не указан, то файл относится именно к
сателлиту, т.е. это невиртуальный файл.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract string FileIsExternalKey { get; }
VB __Копировать
     Protected MustOverride ReadOnly Property FileIsExternalKey As String
    	Get
C++ __Копировать
     protected:
    virtual property String^ FileIsExternalKey {
    	String^ get () abstract;
    }
F# __Копировать
     abstract FileIsExternalKey : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[TaskSatellitePermissionsGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatellitePermissionsGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
