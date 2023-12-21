# PerformanceTestGroup(String, Int32, PerformanceTest[]) - конструктор
Инициализирует новый экземпляр класса
[PerformanceTestGroup](T_Tessa_Diagnostics_PerformanceTestGroup.htm)
##  __Definition
 **Пространство имён:** [Tessa.Diagnostics](N_Tessa_Diagnostics.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public PerformanceTestGroup(
    	string name,
    	int milliseconds,
    	params PerformanceTest[] tests
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	milliseconds As Integer,
    	ParamArray tests As PerformanceTest()
    )
C++ __Копировать
     public:
    PerformanceTestGroup(
    	String^ name, 
    	int milliseconds, 
    	... array<PerformanceTest^>^ tests
    )
F# __Копировать
     new : 
            name : string * 
            milliseconds : int * 
            tests : PerformanceTest[] -> PerformanceTestGroup
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
milliseconds [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
tests [PerformanceTest](T_Tessa_Diagnostics_PerformanceTest.htm)[]
## __См. также
#### Ссылки
[PerformanceTestGroup - ](T_Tessa_Diagnostics_PerformanceTestGroup.htm)
[PerformanceTestGroup -
перегрузка](Overload_Tessa_Diagnostics_PerformanceTestGroup__ctor.htm)
[Tessa.Diagnostics - пространство имён](N_Tessa_Diagnostics.htm)
