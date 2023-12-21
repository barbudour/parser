# GetTessaSpecialFolderDelegate - делегат
Делегат экземпляры которого возвращают путь к специальным папкам Tessa
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate string GetTessaSpecialFolderDelegate(
    	TessaSpecialFolder specialFolder
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function GetTessaSpecialFolderDelegate ( 
    	specialFolder As TessaSpecialFolder
    ) As String
C++ __Копировать
    [NotNullAttribute]
    public delegate String^ GetTessaSpecialFolderDelegate(
    	TessaSpecialFolder specialFolder
    )
F# __Копировать
     [<NotNullAttribute>]
    type GetTessaSpecialFolderDelegate = 
        delegate of 
            specialFolder : TessaSpecialFolder -> string
#### Параметры
specialFolder
[TessaSpecialFolder](T_Tessa_Applications_TessaSpecialFolder.htm)
     Специальная папка для которой требуется получить путь 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Путь к специальной папке
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
