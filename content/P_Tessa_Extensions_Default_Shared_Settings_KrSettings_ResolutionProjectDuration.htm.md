# KrSettings.ResolutionProjectDuration - свойство
Планируемая длительность по умолчанию в днях по бизнес-календарю для задания
проекта резолюции. Указано на один день дольше, чем количество дней по
умолчанию, заполненное в поле "длительность", чтобы дочерняя резолюция в
течение первого дня создавалась бы с запланированной датой, которая
заканчивается раньше, чем у проекта резолюции. По умолчанию значение равно 3.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Settings](N_Tessa_Extensions_Default_Shared_Settings.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public double ResolutionProjectDuration { get; set; }
VB __Копировать
     Public Property ResolutionProjectDuration As Double
    	Get
    	Set
C++ __Копировать
     public:
    property double ResolutionProjectDuration {
    	double get ();
    	void set (double value);
    }
F# __Копировать
     member ResolutionProjectDuration : float with get, set
#### Значение свойства
[Double](https://learn.microsoft.com/dotnet/api/system.double)
##  __См. также
#### Ссылки
[KrSettings - ](T_Tessa_Extensions_Default_Shared_Settings_KrSettings.htm)
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
