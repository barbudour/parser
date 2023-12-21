# AssemblyApplicationPackageBinder - конструктор
Initializes a new instance of the
[AssemblyApplicationPackageBinder](T_Tessa_Applications_Package_AssemblyApplicationPackageBinder.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AssemblyApplicationPackageBinder(
    	[NotNullAttribute] HashCalculateDelegateAsync hashCalculatorAsync,
    	[NotNullAttribute] IApplicationDescriptor applicationDescriptor,
    	[NotNullAttribute] IIgnoredFilesProvider ignoredFilesProvider
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> hashCalculatorAsync As HashCalculateDelegateAsync,
    	<NotNullAttribute> applicationDescriptor As IApplicationDescriptor,
    	<NotNullAttribute> ignoredFilesProvider As IIgnoredFilesProvider
    )
C++ __Копировать
     public:
    AssemblyApplicationPackageBinder(
    	[NotNullAttribute] HashCalculateDelegateAsync^ hashCalculatorAsync, 
    	[NotNullAttribute] IApplicationDescriptor^ applicationDescriptor, 
    	[NotNullAttribute] IIgnoredFilesProvider^ ignoredFilesProvider
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] hashCalculatorAsync : HashCalculateDelegateAsync * 
            [<NotNullAttribute>] applicationDescriptor : IApplicationDescriptor * 
            [<NotNullAttribute>] ignoredFilesProvider : IIgnoredFilesProvider -> AssemblyApplicationPackageBinder
#### Параметры
hashCalculatorAsync
[HashCalculateDelegateAsync](T_Tessa_Applications_HashCalculateDelegateAsync.htm)
     Калькулятор контрольных сумм 
applicationDescriptor
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
     Описатель приложения 
ignoredFilesProvider
[IIgnoredFilesProvider](T_Tessa_Applications_Package_IIgnoredFilesProvider.htm)
     The ignored Files Provider. 
## __См. также
#### Ссылки
[AssemblyApplicationPackageBinder -
](T_Tessa_Applications_Package_AssemblyApplicationPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
