# ScanFileHelper.ShowEditFirstDialog - метод
Отображает диалог редактирования первого файла из objects, причём изображения
"собираются" из всех файлов для поддерживаемых форматов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task ShowEditFirstDialog(
    	IList<IFileObject> objects,
    	ScanFileDialogSettings settings
    )
VB __Копировать
     Public Shared Function ShowEditFirstDialog ( 
    	objects As IList(Of IFileObject),
    	settings As ScanFileDialogSettings
    ) As Task
C++ __Копировать
     public:
    static Task^ ShowEditFirstDialog(
    	IList<IFileObject^>^ objects, 
    	ScanFileDialogSettings^ settings
    )
F# __Копировать
     static member ShowEditFirstDialog : 
            objects : IList<IFileObject> * 
            settings : ScanFileDialogSettings -> Task 
#### Параметры
objects
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileObject](T_Tessa_Files_IFileObject.htm)>
     Файлы, из которых "собирается" редактируемый файл. По завершению редактирования результат сохраняется в первый файл из списка. 
settings
[ScanFileDialogSettings](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
    Настройки диалога сканирования.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ScanFileHelper -
](T_Tessa_Extensions_Platform_Client_ViewModels_ScanFileHelper.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
